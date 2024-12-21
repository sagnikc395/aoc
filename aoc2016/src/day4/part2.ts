// Function to decrypt the room name using the sector ID
function decryptName(encryptedName: string, sectorID: number): string {
  const shift = sectorID % 26;
  return encryptedName
    .split("")
    .map((char) => {
      if (char === "-") {
        return " ";
      } else if (char >= "a" && char <= "z") {
        const newCharCode = ((char.charCodeAt(0) - 97 + shift) % 26) + 97;
        return String.fromCharCode(newCharCode);
      } else {
        return char;
      }
    })
    .join("");
}

// Function to find the sector ID of the room where North Pole objects are stored
function findNorthPoleSectorID(rooms: string[]): number | null {
  for (const room of rooms) {
    const match = room.match(/^([a-z-]+)-(\d+)\[([a-z]+)\]$/);
    if (!match) continue;

    const [, name, sectorIDStr] = match;
    const sectorID = parseInt(sectorIDStr, 10);
    const decryptedName = decryptName(name, sectorID);

    if (decryptedName.includes("northpole")) {
      return sectorID;
    }
  }
  return null;
}

async function main() {
  const file = Bun.file("./input.txt");
  const data = await file.text();
  const items = data.split("\n");

  const northPoleSecId = findNorthPoleSectorID(items);
  if (northPoleSecId !== null) {
    console.log(`Sector ID of the room : ${northPoleSecId}`);
  } else {
    console.log(`No room with 'northpole' found.`);
  }
}

await main();

export {};
