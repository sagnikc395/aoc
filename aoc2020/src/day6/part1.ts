async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const data = buffer.toString();

  const splitGroups = (input: string): string[][] => {
    return input
      .trim()
      .split("\n\n")
      .map((grp) => grp.split("\n"));
  };

  const countUniqueYes = (group: string[]): number => {
    const allAns = new Set(group.join("").split(""));
    return allAns.size;
  };

  const countTotalUnique = (input: string): number => {
    const groups = splitGroups(input);
    return groups.reduce((total, group) => total + countUniqueYes(group), 0);
  };

  console.log(countTotalUnique(data));
}

await main();
