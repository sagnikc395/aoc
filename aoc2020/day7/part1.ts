type BagRule = {
  color: string;
  count: number;
};

function parseRules(rules: string): Map<string, BagRule[]> {
  const bagRules = new Map<string, BagRule[]>();
  const ruleLines = rules.trim().split("\n");

  for (const rule of ruleLines) {
    const [containerColor, contents] = rule.split(" contain ");
    const containerColorParts = containerColor.split(" ").slice(0, -1);
    const containerColorKey = containerColorParts.join(" ");

    if (contents === "no other bags.") {
      continue;
    }

    const contentRules: BagRule[] = contents
      .slice(0, -1)
      .split(", ")
      .map((item) => {
        const [count, color] = item.split("", 2);
        const colorParts = color.split(" ").slice(0, -1);
        const colorKey = colorParts.join(" ");
        return { color: colorKey, count: parseInt(count, 10) };
      });
    bagRules.set(containerColorKey, contentRules);
  }

  return bagRules;
}

function countContainers(rules: string, startBag: string): number {
  const bagRules = parseRules(rules);
  const queue: string[] = [startBag];
  const containers = new Set<string>();

  while (queue.length > 0) {
    const currBag = queue.shift();
    for (const [containerColor, contentRules] of bagRules.entries()) {
      if (contentRules.some((rule) => rule.color === currBag)) {
        containers.add(containerColor);
        queue.push(containerColor);
      }
    }
  }

  return containers.size;
}

async function main() {
  const file = Bun.file("./input.txt");
  const arrBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrBuffer);
  const rules = buffer.toString();
  console.log(countContainers(rules,"shiny gold"));
}

await main();
