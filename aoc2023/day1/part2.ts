const digits: Map<string, number> = new Map([
  ["one", 1],
  ["two", 2],
  ["three", 3],
  ["four", 4],
  ["five", 5],
  ["six", 6],
  ["seven", 7],
  ["eight", 8],
  ["nine", 9],
]);

function findCalibration(input: string): number {
  const lines = input.split("\n");
  let sum = 0;

  for (const line of lines) {
    if (line.trim().length > 0) {
      const words = line.split(/\W+/);
      const firstDigit =
        digits.get(words.find((word) => digits.has(word))!) || 0;
      const lastDigit =
        digits.get(words.reverse().find((word) => digits.has(word))!) || 0;
      const calibrationValue = firstDigit * 10 + lastDigit;
      sum += calibrationValue;
    }
  }

  return sum;
}

async function main() {
  const file = Bun.file("./temp.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const items = buffer.toString();
  let sum = findCalibration(items);

  console.log(sum);
}

await main();
