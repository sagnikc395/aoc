import fs from "fs";

const readPairs = (pair) => {
  return pair
    .trim()
    .split("\n")
    .map((line) => line.split(` `));
};

const getScore = ([opponent, player]) => {
  const scoreForShape = {
    X: 1,
    Y: 2,
    Z: 3,
  };
  const scoreForOutcome = {
    A: { X: 3, Y: 6, Z: 0 },
    B: { X: 0, Y: 3, Z: 6 },
    C: { X: 6, Y: 0, Z: 3 },
  };
  const shapeScore = scoreForShape[player];
  const outcomeScore = scoreForOutcome[opponent][player];

  return shapeScore + outcomeScore;
};

const getPlayerByOutcome = ([opponent, desiredOutcome]) => {
  const shapeForOutcome = {
    A: { X: "Z", Y: "X", Z: "Y" },
    B: { X: "X", Y: "Y", Z: "Z" },
    C: { X: "Y", Y: "Z", Z: "X" },
  };
  const player = shapeForOutcome[opponent][desiredOutcome];

  return player;
};

const getCorrectTotalScore = (input) => {
  return readPairs(input)
    .map((pair) => [pair[0], getPlayerByOutcome(pair)])
    .reduce((total, pair) => total + getScore(pair), 0);
};

const main = () => {
  const input = fs.readFileSync("./input.txt", "utf-8");
  console.log(getCorrectTotalScore(input));
};

main();
