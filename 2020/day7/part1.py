from typing import Dict, List
from dataclasses import dataclass

@dataclass
class BagRule:
    color: str
    count: int

def parse_rules(rules: str) -> Dict[str, List[BagRule]]:
    bag_rules = {}
    rule_lines = rules.strip().split("\n")

    for rule in rule_lines:
        container_color, contents = rule.split(" contain ")
        container_color_parts = container_color.split()[:-1]  # Remove 'bags'/'bag'
        container_color_key = " ".join(container_color_parts)

        if contents == "no other bags.":
            continue

        content_rules = []
        for item in contents[:-1].split(", "):  # Remove period and split
            words = item.split()
            count = int(words[0])
            color_parts = words[1:-1]  # Remove 'bags'/'bag'
            color_key = " ".join(color_parts)
            content_rules.append(BagRule(color=color_key, count=count))

        bag_rules[container_color_key] = content_rules

    return bag_rules

def count_containers(rules: str, start_bag: str) -> int:
    bag_rules = parse_rules(rules)
    queue = [start_bag]
    containers = set()

    while queue:
        curr_bag = queue.pop(0)
        for container_color, content_rules in bag_rules.items():
            if any(rule.color == curr_bag for rule in content_rules):
                containers.add(container_color)
                queue.append(container_color)

    return len(containers)

def main():
    with open("input.txt", "r") as file:
        rules = file.read()
    print(count_containers(rules, "shiny gold"))

if __name__ == "__main__":
    main()
