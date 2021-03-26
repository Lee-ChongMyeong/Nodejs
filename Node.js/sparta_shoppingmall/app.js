const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const router = express.Router();
const mongoose = require("mongoose");
const Todo = require("./models/todo")

// [MongoDB]
mongoose.connect("mongodb://localhost/todo-demo", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));

//// [Get] - 할 일 가져오기
router.get("/todos", async(req, res) =>{
    const todos = await Todo.find().sort("-order").exec();    // 데이터베이스에서 찾아오기

    res.send({ todos });
    /*
        {
            todos : [
                { todoId : ' ~~~',
                 value : '~~~~',
                order : 1, ~~~}
            ]
        }
    */
});



//// [Post] - 할 일 추가
router.post("/todos", async (req, res) => {
    const{ value } = req.body;  // 구조분해 할당
    const maxOrderTodo = await Todo.findOne().sort("-order").exec();    // order을 기준으로 정렬 & 실행
    let order = 1;

    if(maxOrderTodo){   // order 가 있으면
        order = maxOrderTodo.order + 1;
    }

    const todo = new Todo({ value, order});     // value, order 두개를 한번에 저장
    await todo.save();

    res.send({ todo })     // 성공적으로 저장했으면 todo 불러옴
})


//// [Patch]   - 순서 수정, 할일 내용 수정
router.patch("/todos/:todoId", async (req, res) => {
    const { todoId } = req.params;
    const { order, value, done } = req.body;

    const todo = await Todo.findById(todoId).exec();   // DB에서 찾아옴

    if (order) {
        const targetTodo = await Todo.findOne({ order }).exec();
        if (targetTodo) {
            targetTodo.order = todo.order;
            await targetTodo.save();
        }
        todo.order = order;
       // await todo.save();
    }else if (value){
        todo.value = value;
       // await todo.save();
    }else if (done != undefined){
        todo.doneAt = done ? new Date() : null;
       // await todo.save();
    }

    await todo.save();

    res.send({ });
})



//// [Delete] - 삭제
router.delete("/todos/:todoId", async(req, res) =>{
    const { todoId } = req.params;

    await Todo.findByIdAndDelete(todoId).exec();

    res.send({});
})




router.get("/", (req, res) => {
  res.send("Hi!");
});


app.use("/api", bodyParser.json(), router);
app.use(express.static("./assets"));


app.listen(3000, () => {
  console.log("서버가 켜졌어요!");
});