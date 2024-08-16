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
  console.log(n);
});

function solve() {}
