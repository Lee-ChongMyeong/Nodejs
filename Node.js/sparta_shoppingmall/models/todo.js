const mongoose = require("mongoose")

const TodoSchema = new mongoose.Schema({    // Schema는 클래스라서 new 붙여줘야됨.
    value : String,
    doneAt : Date,
    order : Number
});

TodoSchema.virtual("todoId").get(function(){ // virtual model 이란 collection에 정의 되지 않은 field 이지만 정의된 field 처럼 사용할 수 있다.
    return this._id.toHexString();  // mongodb에서 생성된 id는 string이 아니므로,   // this : 모델 자체에 접근할 수 있다.
})                                  // mongoDB의 toHexString() 메서드를 사용하여 형변환

TodoSchema.set("toJSON", {  //TodoSchema 모델이 JSON 형태로 변환이 될때, Virtual Schema를 포함한다.
    virtuals : true,
})

module.exports = mongoose.model("Todo", TodoSchema)


//// [JWT?]
/*

1. JWT는 변조가 불가능 하다.
- 서버가 아니면 변조가 불가능 하다.
- 서버에서 주는 데이터가 1이었는데 내가 2로 바꿔서 서버한테 보내고 싶다(x)

2. 복호화는 어디서든 가능
- JWT 를 암호화라고 부르지 않음, serialize라고 부름(형태를 변환한다)
- JWT를 serialize 다른곳에 보내면은 변조는 불가능 하지만, 그 안에 있는 데이터는 모두 열어 볼 수 있다.

-서버에서는 클라이언트를 구분할 수 있는 고유정보를 담아서 토큰을 발급.
-클라이언는 항사 API 요청할때 토큰을 같이 포함해서 보냄.



*/