async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const items = buffer.toString().split("\n");
  let result = 0;
  for (let item of items) {
    const firstDigit = parseInt(item.match(/\d/)?.[0] || "0", 10);
    const lastDigit = parseInt(item.match(/\d(?!.*\d)/)?.[0] || "0", 10);
    const calValue = firstDigit * 10 + lastDigit;
    result += calValue;
  }

  console.log(result);
}

await main();
