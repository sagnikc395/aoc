async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const items = buffer.toString().split("\n");

  let count = 0;
  for (const password of items) {
    const parts = password.split(":");
    if (parts.length !== 2) {
      continue;
    }

    const [policy, pass] = parts;
    const [range, key] = policy.split(" ");
    let low, upper;
    if (range) {
      [low, upper] = range.split("-");
    } else {
      continue;
    }

    let charCount = 0;
    if (pass) {
      for (let char of pass.trim()) {
        if (char === key) {
          charCount += 1;
        }
      }
    }
    if (charCount >= parseInt(low) && charCount <= parseInt(upper)) {
      count += 1;
    }
  }

  console.log(count);
}

await main();
