const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stout,
});

let n;
rl.on("line", (input) => {
  n = input;
  rl.close();
}).on("close", () => {
  console.log(solve(parseInt(n)));
});
function solve(n) {
  let count = 0;
  let sum = 0;
  let start = 1;

  for (let end = 1; end <= n; end++) {
    sum += end;

    while (sum > n) {
      //같아질때까지
      sum -= start; //앞 숫자를 뺌
      start++;
    }

    if (sum === n) {
      count++;
    }
  }

  return count;
}
