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
    with open('./input.txt','r') as f:
        data = f.read()

    import re
    ans = 0
    # Split the string by "do()"
    do_splits = data.split('do()')
    valid_mul_strings = []
    valid_muls = []
    regex = r"mul\(\d{1,3},\d{1,3}\)"

    # Collect substrings before "don't()" in each split
    for d in do_splits:
        valid_mul_strings.append(d.split("don't()")[0])

    # Extract all valid "mul(x,y)" patterns from valid_mul_strings
    for mvs in valid_mul_strings:
        valid_muls.extend(re.findall(regex, mvs))

    # Process each valid "mul(x,y)" and calculate the result
    for vm in valid_muls:
        numbers = vm[4:-1]  # Remove "mul(" and ")"
        p1, p2 = map(int, numbers.split(','))  # Split and convert to integers
        ans += p1 * p2  # Multiply the numbers and add to the total

    print(ans)



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
