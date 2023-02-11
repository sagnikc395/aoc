import * as fs from "fs";

const main = () => {
  try {
    const data = fs.readFileSync("input.txt", "utf-8");
    const arr = data.split("\n").map((val) => parseInt(val));

    let items = [];

    for (let i = 0; i < arr.length; i++) {
      for (let j = 1; j < arr.length; j++) {
        for (let k = 2; k < arr.length; k++) {
          if (arr[i] + arr[j] + arr[k] === 2020) {
            items.push(arr[i]);
            items.push(arr[j]);
            items.push(arr[k]);
            break;
          }
        }
      }
    }
    console.log(items[0] * items[1] * items[2]);
  } catch (err) {
    console.error(err);
  }
};

main();
