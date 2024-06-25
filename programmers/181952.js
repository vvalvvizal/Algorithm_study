const readline = require("readline");
const rl = readline.createInterface({
  //인터페이스 생성
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let str = "";

rl.on("line", function (line) {
  input = [line];
  rl.close(); //한번 입력 받고 인터페이스 닫음.
}).on("close", function () {
  str = input[0];
  console.log(str);
});
