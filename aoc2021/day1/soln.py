def part1():
    with open('./input.txt','r') as f:
        data = f.read().strip().split('\n')

    measurements = data
    #print(len(data))
    #count = 0

    # for i in range(len(data)-1):
    #     if data[i+1] > data[i]:
    #         count += 1

    # print(count)
    increases = 0
    for i in range(len(measurements)-1):
        current = measurements[i]
        next_depth = measurements[i+1]
        is_increase = next_depth > current
        if is_increase:
            increases += 1
        print(f"{current} -> {next_depth} ({'increased' if is_increase else 'decreased or equal'})")

    print(f"\nTotal measurements: {len(measurements)}")
    print(f"Final count of increases: {increases}")

def part2():
    pass

def main():
    import argparse

    parser = argparse.ArgumentParser(description="AoC 2021 , Day1")
    parser.add_argument("--part1",action='store_true',help='Run Part1')
    parser.add_argument("--part2",action="store_true",help="Run Part2")

    args = parser.parse_args()

    try:
        if args.part1:
            part1()
        elif args.part2:
            part2()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
