def split_groups(input_str: str) -> list[list[str]]:
    return [group.split("\n") for group in input_str.strip().split("\n\n")]

def count_common_yes_ans(group: list[str]) -> int:
    # Convert each answer to a set of characters
    ans_sets = [set(ans) for ans in group]

    # Find intersection of all sets in the group
    # Using * to unpack the list of sets for set.intersection()
    common_ans = set.intersection(*ans_sets)
    return len(common_ans)

def count_total_common_yes_answers(input_str: str) -> int:
    groups = split_groups(input_str)
    return sum(count_common_yes_ans(group) for group in groups)

def main():
    with open("input.txt", "r") as file:
        data = file.read()
    print(count_total_common_yes_answers(data))

if __name__ == "__main__":
    main()
