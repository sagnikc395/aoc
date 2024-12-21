function isTLS(ip: string): boolean {
  // Check for ABBA outside square brackets
  const outsideBrackets = ip.replace(/\[.*?\]/g, "");
  for (let i = 0; i < outsideBrackets.length - 3; i++) {
    const a = outsideBrackets[i];
    const b = outsideBrackets[i + 1];
    const c = outsideBrackets[i + 2];
    const d = outsideBrackets[i + 3];
    if (a === d && b === c && a !== b) {
      return true;
    }
  }

  // Check for ABBA inside square brackets
  const insideBrackets = ip.match(/\[.*?\]/g);
  if (insideBrackets) {
    for (const bracket of insideBrackets) {
      for (let i = 0; i < bracket.length - 3; i++) {
        const a = bracket[i];
        const b = bracket[i + 1];
        const c = bracket[i + 2];
        const d = bracket[i + 3];
        if (a === d && b === c && a !== b) {
          return false;
        }
      }
    }
  }

  // If no ABBA is found inside square brackets, return true
  return true;
}

const file = Bun.file("./input.txt");
const data = await file.text();

const count = data.split("\n").filter(isTLS).length;
console.log(count);

export {};
