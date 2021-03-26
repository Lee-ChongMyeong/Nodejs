const jwt = require("jsonwebtoken")
const User = require("../models/user")  // User모델이 불러와짐

module.exports = (req, res, next) => {
    console.log("여기를 지나쳤어요")

    // token 에 user : userId 값을 보냄 -> HTTP header에 담아서 -> Authorization 헤더로 전달 받음 -> split 해서 필요한 값인 tokenValue() 를 얻어냄.
    // tokenValue 값은 암호화한 값으로 저장됨   / 즉, tokenValue 안에 user : userId 값이 들어가 있음 -> 

    const { authorization } = req.headers;   // headers안에 header 가포함
                                            // 프론트엔드에 대문자로 보내도 소문자로 가게됨
    const [tokenType, tokenValue] = authorization.split(' ');    // 공백을 기준으로 배열로 반환
    console.log(tokenValue);                                     // tokenValue가 우리가 원하는 값

    if (tokenType !== 'Bearer'){    // tokenType 이 Bearer 일때만 작동
        res.status(401).send({
            errorMessage : '로그인 후 사용하세요',
        });
        return; // next가 호출 안되게
    }

    try { 
        const { userId } = jwt.verify(tokenValue, "my-secret-key")  // 복호화 하게됨, 토큰데이터가 유효한지 아닌지
        console.log("userID 값 : ", userId)    // 왜 ? userId : user.userId 형태로 안나오는가? 왜 오직 User.userId 값만 나오게 되는가

        User.findById(userId).exec().then((user) => {
            res.locals.user = user;
            next();// 미들웨어는 next가 반드시 호출되어야 한다.
        });

    }catch(error){
        res.status(401).send({
            errorMessage : "로그인 후 사용하세요",
        })
        return;
    }
}

