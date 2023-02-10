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

console.log(Math.max(...solve("./input.txt")));
