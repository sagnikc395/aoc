const file = Bun.file("./input.txt");
const data = await file.text();

const parsedData = data.split("\n").map((item) => Number(item));

const freqMap: Record<number, number> = {};

let curFreq = 0;
let found = false;
while (!found) {
  for (const item of parsedData) {
    curFreq += item;

    if (curFreq in freqMap) {
      console.log("First frequency reached twice:", curFreq);
      found = true;
      break;
    }

    freqMap[curFreq] = 1;
  }
}
