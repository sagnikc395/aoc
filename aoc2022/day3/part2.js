import fs from "fs";

const readFile = (input) => {
  const file = fs.readFileSync(input, "utf-8");
  const readData = file.trim().split("\n");
  return readData;
};

const splitItems = (input) => {
  return [input.slice(0, input.length / 2), input.slice(input.length / 2)];
};

const findFirstCommonItem = (strings) => {
  const sets = strings.map((str) => new Set(str.split("")));
  const commonLetters = [...sets[0]].filter((ch) => {
    return sets.every((set) => set.has(ch));
  });
  return commonLetters[0];
};

const letterToPriority = (ch) => {
  const letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  return letters.indexOf(ch) + 1;
};

const groupItems = (arr) => {
  const groups = [];
  for (let i = 0; i < arr.length; i += 3) {
    groups.push(arr.slice(i, i + 3));
  }
  return groups;
};

const getSumOfGroupedPriorities = (input) => {
  return groupItems(splitItems(input))
    .map(findFirstCommonItem)
    .map(letterToPriority)
    .reduce((a, b) => a + b, 0);
};

console.log(getSumOfGroupedPriorities("./input.txt"));
