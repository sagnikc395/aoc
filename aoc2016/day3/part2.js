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
      const item1 = String(tlens[0]);
      const item2 = String(tlens[1]);
      const item3 = String(tlens[2]);

      if (
        item1.slice(-2) === item2.slice(-2) &&
        item2.slice(-2) === item3.slice(-2) &&
        item1.slice(-2) === item3.slice(-2)
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
