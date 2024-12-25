def part1():
    with open('./input.txt','r') as f:
        data = f.read().strip().split('\n')

    elf_calorie_counter = {}
    elf_counter = 0

    sum = 0
    for item in data:
        if item != '':
            sum += int(item)
            elf_calorie_counter[elf_counter] = sum
        else:
            elf_counter += 1
            sum = 0

    highest_elf = max(elf_calorie_counter.items(), key=lambda item: item[1])
    print(highest_elf)

def part2():
    with open('./input.txt','r') as f:
        data = f.read().strip().split('\n')

    elf_calorie_counter = {}
    elf_counter = 0

    sum = 0
    for item in data:
        if item != '':
            sum += int(item)
            elf_calorie_counter[elf_counter] = sum
        else:
            elf_counter += 1
            sum = 0

    top_three_highest_elf =  sorted(elf_calorie_counter.items(),key=lambda item: item[1],reverse=True)[:3]

    result = 0
    for _, v in top_three_highest_elf:
        result += v
    print(result)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="AoC 2022, Day1")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")

    args = parser.parse_args()

    if args.part1:
        part1()
    elif args.part2:
        part2()

if __name__ == '__main__':
    main()
