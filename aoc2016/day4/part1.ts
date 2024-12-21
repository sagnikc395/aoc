// Function to check if a room is real based on its checksum
function isRealRoom(name: string, checksum: string): boolean {
  // Remove dashes and count letter frequencies
  const letterCounts: { [key: string]: number } = {};
  for (const char of name.replace(/-/g, "")) {
    letterCounts[char] = (letterCounts[char] || 0) + 1;
  }

  // Sort letters by frequency and then alphabetically
  const sortedLetters = Object.keys(letterCounts).sort((a, b) => {
    const diff = letterCounts[b] - letterCounts[a];
    return diff === 0 ? a.localeCompare(b) : diff;
  });

  // Generate the checksum from the five most common letters
  const generatedChecksum = sortedLetters.slice(0, 5).join("");

  return generatedChecksum === checksum;
}

// Function to parse the input and sum sector IDs of real rooms
function sumOfRealRoomSectorIDs(rooms: string[]): number {
  let sum = 0;

  for (const room of rooms) {
    const match = room.match(/^([a-z-]+)-(\d+)\[([a-z]+)\]$/);
    if (!match) continue;

    const [, name, sectorID, checksum] = match;
    if (isRealRoom(name, checksum)) {
      sum += parseInt(sectorID, 10);
    }
  }

  return sum;
}

async function main() {
  const file = Bun.file("./input.txt");
  const data = await file.text();
  const items = data.split("\n");

  const totalSectorIDSum = sumOfRealRoomSectorIDs(items);
  console.log(`Sum of sector IDs for real rooms: ${totalSectorIDSum}`);
}

await main();

export {};
