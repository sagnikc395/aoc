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

  const countCommonYesAns = (group: string[]): number => {
    const ansSets = group.map((ans) => new Set(ans));
    const commonAns = ansSets.reduce((common, set) => {
      return new Set([...common].filter((ans) => set.has(ans)));
    }, ansSets[0]);

    return commonAns.size;
  };

  const countTotalCommonYesAnswers = (input: string): number => {
    const groups = splitGroups(input);
    return groups.reduce(
      (total, group) => total + countCommonYesAns(group),
      0
    );
  };

  console.log(countTotalCommonYesAnswers(data));
}

await main();
