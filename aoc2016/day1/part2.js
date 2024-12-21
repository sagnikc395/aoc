const file = Bun.file("./input.txt");
const data = await file.text();
const movements = data.split(",").map((m) => m.trim());

const directions = ["N", "E", "S", "W"];

let currDirections = 0;
const rotate = (curr) => {
  if (curr === "R") {
    currDirections = (currDirections + 1) % directions.length;
  } else {
    currDirections = (currDirections + 3) % directions.length;
  }
};

let coords = [0, 0];
const move = {
  N: (v) => [0, v],
  E: (v) => [v, 0],
  S: (v) => [0, -v],
  W: (v) => [-v, 0],
};

const visitedPositions = new Set(["0,0"]);
let firstRepeat = null;

function checkAndAddPosition(x, y) {
  const posKey = `${x},${y}`;
  if (visitedPositions.has(posKey) && !firstRepeat) {
    firstRepeat = [x, y];
  }
  visitedPositions.add(posKey);
}

for (const movement of movements) {
  if (firstRepeat) break;

  const turn = movement[0];
  const walk = parseInt(movement.slice(1), 10);

  rotate(turn);

  const facing = directions[currDirections];
  const [dx, dy] = move[facing](walk);

  // Move one step at a time and check each position
  const stepX = Math.sign(dx);
  const stepY = Math.sign(dy);
  for (let i = 0; i < Math.abs(dx); i++) {
    coords[0] += stepX;
    checkAndAddPosition(coords[0], coords[1]);
    if (firstRepeat) break;
  }
  if (firstRepeat) break;
  for (let i = 0; i < Math.abs(dy); i++) {
    coords[1] += stepY;
    checkAndAddPosition(coords[0], coords[1]);
    if (firstRepeat) break;
  }
}

const manhattan = (a, b) => {
  let distance = 0;
  const dimension = Math.max(a.length, b.length);
  for (let i = 0; i < dimension; i++) {
    distance += Math.abs((b[i] || 0) - (a[i] || 0));
  }
  return distance;
};

console.log("Part 1 - Final position distance:", manhattan([0, 0], coords));
console.log(
  "Part 2 - First repeat position distance:",
  firstRepeat ? manhattan([0, 0], firstRepeat) : "No repeat found"
);
