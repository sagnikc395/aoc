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

const checkPairs = (pairing) => {
  const pair1 = pairing[0];
  const pair2 = pairing[1];
  const a_range = checkRange(...pair1);
  const b_range = checkRange(...pair2);
  const maxsize = Math.max(a_range.length, b_range.length);
  const unique = [...new Set(a_range.concat(b_range))];
  return unique.length === maxsize;
};

const main = () => {
  const inputFile = "./input.txt";
  let count = 0;
  readFile(inputFile).map((line) => {
    const pairTuples = makePairs(line);
    if (checkPairs(pairTuples)) {
      count += 1;
    }
  });
  console.log(count);
};

main();
