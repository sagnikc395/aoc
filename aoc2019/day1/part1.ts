import fs from "fs";

const main = () => {
  try {
    const data = fs.readFileSync("./input.txt", "utf-8");
    const arr = data
      .split("\n")
      .map((item) => parseInt(item))
      .filter(Boolean);
    let fuelRequired = 0;
    arr.forEach((item) => {
      item = Math.floor(parseFloat(item) / 3);
      item = item - 2;
      fuelRequired += item;
    });
    console.log(fuelRequired);
  } catch (err) {
    console.error(err);
  }
};

main();
