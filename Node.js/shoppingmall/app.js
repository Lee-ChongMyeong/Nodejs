const express = require("express");
const mongoose = require("mongoose");
const User = require("./models/user");
const jwt = require("jsonwebtoken");
const authMiddleware = require("./middlewares/auth-middleware")
const Goods = require("./models/goods");
const Cart = require("./models/cart");
const joi = require("joi");
const Joi = require("joi");

const app = express();
const router = express.Router();

/*
const postUserSchema = Joi.object({
    nickname : Joi.string().required(),
    email : Joi.string().email().required(),
    password : Joi.string().required(),
    confirmPassword : Joi.string().required(),
});
*/


//// [MongoDB]
mongoose.connect("mongodb://localhost/shopping-demo", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));


app.use("/api", express.urlencoded({ extended: false }), router);
app.use(express.static("assets"));



//// [Post - 회원가입]
router.post("/users", async (req, res) => {
    const { nickname, email, password, confirmPassword} = req.body; 

    if (password !== confirmPassword) {
        res.status(400).send({
            errorMessage : '패스워드가 패스워드 확인란과 동일하지 않습니다.',
        }); // 400 : bad request
        return; // 리턴하지 않으면 패스워드가 다르더라도 밑에 코드가 실행됨.
    }

    
    const existUsers = await User.findOne({    // User 몽구스 모델에서, find를 함으로써 값을 여러개 가져옴(조건 맞는것 - 이메일이 겹치거나 닉네임이 겹칠때)
        $or : [{ email }, { nickname }],    // 존재하는 email or nickname 이 있는지 
    });
    if (existUsers){// NOTE: 보안을 위해 인증 메세지는 자세히 설명하지 않는것을 원칙으로 한다:
        res.status(400).send({
            errorMessage : '이미 가입된 이메일 또는 닉네임이 있습니다.',
        });
        return; // error가 났으면 끝난거임.
    }

    const user = new User({ email, nickname, password}) // 데이터 베이스에 저장
    await user.save();

    res.status(201).send({});
});


//// [Post - 로그인]
router.post("/auth", async (req, res) => {
  const { email, password} = req.body;

  const user = await User.findOne({ email, password}).exec();

  if (!user || password !== user.password) {
      res.status(400).send({
          errorMessage : '이메일 또는 패스워드가 잘못됐습니다.'
      });
      return;
  }

  const token = jwt.sign({ userId : user.userId }, "my-secret-key")    // userId 키를 가진곳에 넣어야됨.
                                                                       // 로그인 할 때 해당하는 userId를 암호화
  res.send({                                                            // userId : user.Id 을 token 에 담고 출발~ 
      token, 
  });
});


//// [미들웨어]
router.get("/users/me", authMiddleware, async(req, res) =>{ // /users/me 경로도 들어올때만 authMiddleware 로 붙게됨
    console.log(res.locals);
    const { user } = res.locals;    //user 변수에 res.locals 라는 객체 안에 있는 user라는 키가 구조 분해 할당이 되서 값이 들어가게 됨
    console.log(user);              // 사용자 정보가 들어가 있음
    
    
    //res.status(400).send({  // status 400 : bad request(실패함)
    res.send({  // express는 기본 status 코드를 200으로 줌
        user : user.email,
        nickname : user.nickname,
    })  // 로그를 남긴다는 행위를 로깅이라고 함. 로깅을 하는 행위는 개발자가 버그를 찾기 쉽도록      
})      // 데이터를 남겨놓는것임, 로깅을 할 때 조차 password 값은 아무리 암호화가 되었다해도 남기면 안되는 값임.




/**
 * 내가 가진 장바구니 목록을 전부 불러온다.
 */
 router.get("/goods/cart", authMiddleware, async (req, res) => {
    const { userId } = res.locals.user;
  
    const cart = await Cart.find({
      userId,
    }).exec();
  
    const goodsIds = cart.map((c) => c.goodsId);
  
    // 루프 줄이기 위해 Mapping 가능한 객체로 만든것
    const goodsKeyById = await Goods.find({
      _id: { $in: goodsIds },
    })
      .exec()
      .then((goods) =>
        goods.reduce(
          (prev, g) => ({
            ...prev,
            [g.goodsId]: g,
          }),
          {}
        )
      );
  
    res.send({
      cart: cart.map((c) => ({
        quantity: c.quantity,
        goods: goodsKeyById[c.goodsId],
      })),
    });
  });

/**
 * 장바구니에 상품 담기.
 * 장바구니에 상품이 이미 담겨있으면 갯수만 수정한다.
 */
 router.put("/goods/:goodsId/cart", authMiddleware, async (req, res) => {
    const { userId } = res.locals.user;
    const { goodsId } = req.params;
    const { quantity } = req.body;
  
    const existsCart = await Cart.findOne({
      userId,
      goodsId,
    }).exec();
  
    if (existsCart) {
      existsCart.quantity = quantity;
      await existsCart.save();
    } else {
      const cart = new Cart({
        userId,
        goodsId,
        quantity,
      });
      await cart.save();
    }
  
    // NOTE: 성공했을때 응답 값을 클라이언트가 사용하지 않는다.
    res.send({});
  });

/**
 * 장바구니 항목 삭제
 */
 router.delete("/goods/:goodsId/cart", authMiddleware, async (req, res) => {
    const { userId } = res.locals.user;
    const { goodsId } = req.params;
  
    const existsCart = await Cart.findOne({
      userId,
      goodsId,
    }).exec();
  
    // 있든 말든 신경 안쓴다. 그냥 있으면 지운다.
    if (existsCart) {
      existsCart.delete();
    }
  
    // NOTE: 성공했을때 딱히 정해진 응답 값이 없다.
    res.send({});
  });

/**
 * 모든 상품 가져오기
 * 상품도 몇개 없는 우리에겐 페이지네이션은 사치다.
 * @example
 * /api/goods
 * /api/goods?category=drink
 * /api/goods?category=drink2
 */
 router.get("/goods", authMiddleware, async (req, res) => {
    const { category } = req.query;
    const goods = await Goods.find(category ? { category } : undefined)
      .sort("-date")
      .exec();
  
    res.send({ goods });
  });

  /**
 * 상품 하나만 가져오기
 */
router.get("/goods/:goodsId", authMiddleware, async (req, res) => {
    const { goodsId } = req.params;
    const goods = await Goods.findById(goodsId).exec();
  
    if (!goods) {
      res.status(404).send({});
    } else {
      res.send({ goods });
    }
  });



//// [Port]
app.listen(4000, () => {
  console.log("서버가 요청을 받을 준비가 됐어요");
});