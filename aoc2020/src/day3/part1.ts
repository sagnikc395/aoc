async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const data = buffer.toString().split("\n");

  const width = data[0].length;
  const height = data.length;

  let treeCnt = 0;
  let x = 0;
  let y = 0;

  while (y < height) {
    const currentX = x % width;
    const currntLine = data[y];

    if (currntLine[currentX] === "#") {
      treeCnt++;
    }

    x += 3;
    y += 1;
  }
  console.log(treeCnt);
}

await main();
