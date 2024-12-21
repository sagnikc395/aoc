const file = Bun.file("./input.txt");
const data = await file.text();

const parsedData = data.split('\n').map((item) => Number(item));

let result = 0;

parsedData.forEach((item) => {
  result += item;
})

console.log(result);