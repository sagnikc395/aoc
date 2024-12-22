async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const data = buffer.toString().split("\n");

  const width = data[0].length;
  const height = data.length;

  const slopes = [
    { dx: 1, dy: 1 },
    { dx: 3, dy: 1 },
    { dx: 5, dy: 1 },
    { dx: 7, dy: 1 },
    { dx: 1, dy: 2 },
  ];

  let result = 1;

  for (const slope of slopes) {
    let treeCnt = 0;
    let x = 0;
    let y = 0;
    while (y < height) {
      const currentX = x % width;
      const currntLine = data[y];

      if (currntLine[currentX] === "#") {
        treeCnt++;
      }

      x += slope.dx;
      y += slope.dy;
    }

    result *= treeCnt;
  }
  console.log(result);
}

await main();
