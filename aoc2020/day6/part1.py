def split_groups(input_str: str) -> list[list[str]]:
    return [group.split("\n") for group in input_str.strip().split("\n\n")]

def count_unique_yes(group: list[str]) -> int:
    # Join all answers in group and convert to set of individual characters
    all_answers = set(''.join(group))
    return len(all_answers)

def count_total_unique(input_str: str) -> int:
    groups = split_groups(input_str)
    return sum(count_unique_yes(group) for group in groups)

def main():
    with open("input.txt", "r") as file:
        data = file.read()
    print(count_total_unique(data))

if __name__ == "__main__":
    main()
