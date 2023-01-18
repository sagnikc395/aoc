const fs = require("fs");

const calculateFuel = (input) => {
  return Math.floor(parseFloat(input) / 3) - 2;
};

const main = () => {
  try {
    const data = fs.readFileSync("./input.txt", "utf-8");
    const arr = data
      .split("\n")
      .map((item) => parseInt(item))
      .filter(Boolean);
    let totalTempFuel = 0;
    arr.forEach((item) => {
      let temp = calculateFuel(item);
      while (temp > 0) {
        totalTempFuel += temp;
        temp = calculateFuel(temp);
      }
    });
    console.log(totalTempFuel);
  } catch (err) {
    console.error(err);
  }
};

main();
