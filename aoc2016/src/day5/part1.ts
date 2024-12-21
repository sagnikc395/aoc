import { createHash } from "crypto";

function findPassword(doorID: string): string {
  let password = "";
  let index = 0;

  while (password.length < 8) {
    const hash = createHash("md5")
      .update(doorID + index)
      .digest("hex");

    if (hash.startsWith("00000")) {
      password += hash[5];
    }

    index++;
  }

  return password;
}

const input = "uqwqemis";
const password = findPassword(input);
console.log(`The password is: ${password}`);

export {};
