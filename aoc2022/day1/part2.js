import fs from "fs";

const calorieSum = (nums) => nums.reduce((a, b) => a + b, 0);

const solve = (fileName) => {
  const fileContent = fs.readFileSync(fileName, "utf-8");
  const numbers = fileContent
    .split("\n\n")
    .map((line) => line.split("\n").map(Number))
    .map(calorieSum);
  return numbers;
};

const top3 = (input) => {
  const t = solve(input)
    .sort((a, b) => b - a)
    .slice(0, 3);
  return calorieSum(t);
};

console.log(top3("./input.txt"));
