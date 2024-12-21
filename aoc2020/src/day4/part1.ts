async function main() {
  const file = Bun.file("./test.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const data = buffer.toString().split("/\n\s*\n/");

  console.log(data);
}

await main();
