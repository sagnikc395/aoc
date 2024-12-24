def part1():
    with open('./input.txt','r') as f:
        content = f.read().strip()

    floor = 0
    for char in content:
        if char == '(':
            floor+=1
        elif char == ')':
            floor -=1

    print(floor)

def part2():
    floor = 0
    count = 0
    with open('./input.txt','r') as f:
        content = f.read().strip()

    for char in content:
        if char == '(':
            floor +=1
            count += 1
        elif char == ')':
            if floor < 0:
                print(count)
                break
            else:
                floor -=1
                count +=1

def main():
    import argparse

    parser = argparse.ArgumentParser(description="AoC 2015, Day1")
    parser.add_argument('--part1',action='store_true',help='Run part1 solution')
    parser.add_argument('--part2',action='store_true',help='Run part2 solution')

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
