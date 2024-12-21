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
  N: (v) => (coords[1] += v),
  E: (v) => (coords[0] += v),
  S: (v) => (coords[1] -= v),
  W: (v) => (coords[0] -= v),
};

movements.forEach((movement) => {
  const turn = movement[0];
  const walk = parseInt(movement.slice(1), 10);

  rotate(turn);

  const facing = directions[currDirections];
  move[facing](walk);
});

const manhattan = (a, b) => {
  let distance = 0;
  const dimension = Math.max(a.length, b.length);
  for (let i = 0; i < dimension; i++) {
    distance += Math.abs((b[i] || 0) - (a[i] || 0));
  }
  return distance;
};

console.log(manhattan([0, 0], coords));
