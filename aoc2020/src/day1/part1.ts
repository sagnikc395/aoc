async function main() {
  // Read the input file and convert it to an array of numbers
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const items = buffer.toString().split("\n");

  // Initialize an empty Map
  let map = new Map<number, number>();

  // Iterate through the array of numbers
  for (const item of items) {
    // Convert the string to a number
    const num = parseInt(item);

    // Calculate the complement
    const change = 2020 - num;

    // Check if the complement is already in the Map
    if (!map.has(change)) {
      // If not, add the current number to the Map with its complement as the key
      map.set(num, change);
    } else {
      // If the complement is found, we have two numbers that sum up to 2020
      console.log(`Items ${change} and ${num} are matches`);
      console.log(change * num); // Print the product of the two numbers
    }
  }
}

await main();
