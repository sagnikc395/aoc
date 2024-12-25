def part1():
    with open('./input.txt','r') as f:
        data = f.read()

    import re
    ans = 0
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

    for match in matches:
        parts = match[4:-1]
        p1,p2 = map(int,parts.split(','))
        ans += p1 * p2

    print(ans)



def part2():
    raise NotImplementedError()



def main():
    import argparse
    parser = argparse.ArgumentParser(description="AoC 2024, Day3")

    parser.add_argument("--part1",action="store_true",help="Run Part1")
    parser.add_argument("--part2",action="store_true",help="Run Part2")

    args = parser.parse_args()

    if not(args.part1 or args.part2):
        print("Please provide input flags")
        return

    if args.part1:
        part1()
    if args.part2:
        part2()


if __name__ == '__main__':
    main()
