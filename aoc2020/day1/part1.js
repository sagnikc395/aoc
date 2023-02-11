import * as fs from "fs";

const main = () => {
  try {
    const data = fs.readFileSync("input.txt", "utf-8");
    const arr = data.split("\n").map((val) => parseInt(val));

    let items = [];

    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++) {
        if (i != j) {
          if (arr[i] + arr[j] === 2020) {
            items.push(arr[i]);
            items.push(arr[j]);
            break;
          }
        }
      }
    }
    console.log(items[0] * items[1]);
  } catch (err) {
    console.error(err);
  }
};

main();
