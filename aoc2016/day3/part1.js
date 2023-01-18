const fs = require("fs");

const main = () => {
  try {
    const data = fs.readFileSync("input.txt", "utf-8");
    const arr = data.split("\n").map((item) => item.trim());
    let possible = 0;

    arr.forEach((items) => {
      const tlens = items
        .split(" ")
        .map((item) => parseInt(item))
        .filter(Boolean);

      const item1 = tlens[0];
      const item2 = tlens[1];
      const item3 = tlens[2];

      if (
        item1 + item2 > item3 &&
        item1 + item3 > item2 &&
        item2 + item3 > item1
      ) {
        possible += 1;
      }
    });
    console.log(possible);
  } catch (err) {
    console.error(err);
  }
};

main();
