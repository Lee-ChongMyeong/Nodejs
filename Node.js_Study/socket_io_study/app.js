const socketIo = require("socket.io");  
const express = require("express");// http 모듈을 기반으로 좀 더 코드를 덧붙여 만든 라이브러리. express는 http 모듈을 상속받는다.   
                                   // express가 이 http 모듈의 자식같은 개념
const Http = require("http");   // http 모듈 기반으로 express랑 socket.io 같이 포함해서 실행가능
                                // node.js에서 기본적으로 제공하는 웹서버 모듈
console.log(Http)

const app = express();          // express app 만듬 [ 그말인 즉슨, http에 추가적으로, 한 서버에 서버가 2개 만들어짐 ]
const http = Http.createServer(app); // 이 Http.createServer가 지금 인자로 받고 있는 이거는, 다른 Http 서버를 받아서 확장 할 수 있게 도와줌
                                     // 다른 http서버를 ( ) 안에 넣으면 또하나로 합쳐진 서버가 완성이됨.
                                     // http 서버를 기반으로 만들어지지 않은 라이브러리도 있으므로, 주의해서 써야됨
                                     // http 서버랑 express 서버랑 함칠 수 있다.


                            // 서버를 생성함 (서버를 실행하는 부분)
const io = socketIo(http, { // socketIo 부분이 서버 실행하는 부분. 3000 포트로 지금 소켓을 실행
    cors : {                //첫번째 인자로 들어온게 숫자가 아니고 http 서버이면 http 서버에다 socketIo를 연결하는 router를 (express랑 비슷하게 ) 자동으로 붙입니다. (http 서버로 알아서 붙여줌)
                            // 저장을 하면 express도 쓰고 socketIo도 쓰고 (합쳐지는 기반은 HTTP 서버)
        origin : "*",        // origin : 여기에 명시된 서버만(호스트만) 내 서버로 연결할 거야
        methods : ["GET", "POST"] // * : 모든 문자열을 허락한다.  , Get method 와 Post method만 허용, Delete, Patch는 안됨
    },                  
});


                            // 3)
http.listen(3000, () => {   // http 서버가 지금 중심이기 때문에 이걸 키는것임.
    console.log("서버가 켜졌습니다.! ") // express가 http 모듈을 확장하기 때문에 app.listen 과 비슷하게 생김
})

app.get("/test", (req, res) => {    // express가 잘 켜져있는지 확인
    res.send("익스프레스가 잘 켜져 있습니다.");
})



// 서버 연결(생성)하고 써먹는곳       // 서버입장에서는 되게 큰 공간이 있고 누군가 "어 나 너네 꺼 연결할래" 이러면 소켓을 하나할당해 주는 것임. 그래서 연결된 소켓이 하나 생겼고, 또 누가 나 연결할래 이러면 또 추가됨.
                                    // 연결을 할때마다 socket이 하나 하나 생김 , 현재 socket이랑 연결함.  연결된 소켓이 여기에 할당됨
io.on("connection", (socket) => {   // 누군가 "나 가갈래" 이러고 연결을 끊으면, 저한테 할당되어 있는 소켓을 다시 원래 있던 자리에 안쓰는 곳에 놓음, 이런식으로 소켓을 관리
    console.log("새로운 소켓이 연결됐어요!");    // F12눌러서 확인해보면,  프론트엔드(클라이언트)에서는 계속 연결 요청을 함 (계속 재시도함)
                                                // 그렇기 때문에 언제든 연결이됨. [ 서버가 죽더라도 클라이언트는 연결 요청], [ 프론트 엔드 재시작 안해도 알아서 연결]
    socket.send("너 연결 잘 됐어!.")   // socket.send 하면 지금 연결된 소켓에 연결할 수 있음 
                                    // send는 index.html의 메세지 이벤트 핸들러로 감
                                    // 전기가 항상 공급되고 있다가 플로그를 딱 꽂은게 이 브라우저에서 서버로 연결을 딱 한것임. 전기를 줌(데이터)
    socket.emit("customEventName", "새로운 이벤트인가?")


    // socket.send : 항상 메시지 이벤트 헨들러로 감.
    //
    //socket.on("message", (data) => {
    //    console.log(data);
    //  });
    //
    //
    // socket.emit : emit을 쓰면 커스텀 이벤트를 만들수 있다.
    //
    // socket.on("customEventName", (data) => {
    //     console.log("커스텀이벤트네임 : ", data);
    // });
});


// 1) socket io 서버 실행 --> 2) express 서버 실행 --> 3) http 서버 실행 
// http 라는 모듈을 기반으로 express랑 socket.io 둘다 같이 포함해서 실행할 수 있다.