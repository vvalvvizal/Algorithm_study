const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input = line.trim().split(" ").map(Number);
  rl.close();
}).on("close", () => {
  //[0]x+[1]y=[2]
  //[3]x+[4]y=[5]
  console.log(input);

  // i와 j의 범위를 적절히 설정합니다.
  for (let i = -999; i <= 999; i++) {
    for (let j = -999; j <= 999; j++) {
      if (
        input[0] * i + input[1] * j === input[2] &&
        input[3] * i + input[4] * j === input[5]
      ) {
        console.log(i, j);
        return;
      }
    }
  }
});
