async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const items = buffer.toString().split("\n").map(Number);

  for (const item of items) {
    for (const item2 of items) {
      for (const item3 of items) {
        if (item !== item2 && item2 !== item3 && item !== item3) {
          if (item + item2 + item3 === 2020) {
            console.log(item * item2 * item3);
            break;
          }
        }
      }
    }
  }
}

await main();
