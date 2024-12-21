import { createHash } from "crypto";

function findPasswordWithPosition(doorID: string): string {
  const password = Array(8).fill("_"); // Start with an empty password
  let index = 0;
  let filledPositions = 0;

  while (filledPositions < 8) {
    const hash = createHash("md5")
      .update(doorID + index)
      .digest("hex");

    if (hash.startsWith("00000")) {
      const position = parseInt(hash[5], 10);

      if (position >= 0 && position < 8 && password[position] === "_") {
        password[position] = hash[6];
        filledPositions++;
      }
    }

    index++;
  }

  return password.join("");
}

// Example usage:
const doorID = "uqwqemis"; // Replace with your actual Door ID
const password = findPasswordWithPosition(doorID);
console.log(`The password is: ${password}`);

export {};
