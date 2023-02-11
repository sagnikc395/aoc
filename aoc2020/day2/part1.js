import fs from "fs";

const main: any = () => {
  try {
    const data: string[] = fs.readFileSync("input.txt", "utf-8").split("\n");
    let valid: number = 0;
    data.forEach((passwd) => {
      const args = passwd.split(":");
      const item1 = args[0].split(" ");
      const pass = args[1];
      const range = item1[0].split("-");
      const low = parseInt(range[0]);
      const high = parseInt(range[1]);
      const key = item1[1];

      let count: number = 0;
      for (let i = 0; i < pass.length; i++) {
        if (pass[i] === key) {
          count += 1;
        }
      }
      if (count >= low && count <= high) {
        valid += 1;
      }
    });
    console.log(valid);
  } catch (err) {
    console.error(err);
  }
};

main();
