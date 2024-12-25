def part1():
    pass

def part2():
    pass




def main():
    import argparse

    parser = argparse.ArgumentParser(description="AoC 2017, Day1")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")

    args = parser.parse_args()

    if args.part1:
        part1()
    elif args.part2:
        part2()

if __name__ == '__main__':
    main()
