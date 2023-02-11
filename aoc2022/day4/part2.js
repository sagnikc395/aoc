import fs, { read } from "fs";

const readFile = (input) => {
  const file = fs.readFileSync(input, "utf-8").split("\n");
  return file;
};

const makePairs = (line) => {
  const elfs = line.split(",");
  const elf1Args = elfs[0].split("-").map((item) => Number(item));
  const elf2Args = elfs[1].split("-").map((item) => Number(item));
  return [elf1Args, elf2Args];
};

const checkRange = (from, to, inclusive = true) => {
  if (to < from) {
    [from, to] = [to, from];
  }
  const size = to - from + (inclusive ? 1 : 0);
  return Array(size)
    .fill()
    .map((_, i) => i + from);
};

const intersection = (...arrs) => {
  const counts = new Map();
  for (let arr of arrs) {
    const unique = [...new Set(arr)];

    for (let val of unique) {
      if (!counts.has(val)) {
        counts.set(val, 0);
      }
      const current_count = counts.get(val);
      counts.set(val, current_count + 1);
    }
  }

  const intersected = [...counts.entries()]
    .filter(([key, count]) => count === arrs.length)
    .map(([key]) => key);

  return intersected;
};

const intersectingPairs = ([...pairing]) => {
  const a_range = checkRange(...pairing[0]);
  const b_range = checkRange(...pairing[1]);
  const overLapping = intersection(a_range, b_range);
  return overLapping.length > 0;
};

const main = () => {
  const inputFile = "./input.txt";
  let count = 0;
  readFile(inputFile).map((line) => {
    const pairTuples = makePairs(line);
    if (intersectingPairs(pairTuples)) {
      count += 1;
    }
  });
  console.log(count);
};

main();
