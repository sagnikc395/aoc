async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const data = buffer.toString().split("\n");
  // console.log(data);
  let count = 0;
  for (const pass of data) {
    const [policy, password] = pass.split(":");
    const [lower, upp] = policy.split("-");
    const [upper, key] = upp.split(" ");

    if (
      password[parseInt(lower)] === key &&
      password[parseInt(upper)] !== key
    ) {
      count += 1;
    } else if (
      password[parseInt(lower)] !== key &&
      password[parseInt(upper)] === key
    ) {
      count += 1;
    }
  }
  console.log(count);
}

await main();
