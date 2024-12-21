def is_valid_sequence(arr):
    if len(arr) < 2:
        return True

    is_increasing = arr[1] > arr[0]

    for i in range(1,len(arr)):
        diff = arr[i] - arr[i-1]

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        if is_increasing and diff < 0:
            return False
        if not is_increasing and diff > 0:
            return False

    return True


def tolerate_single_bad(arr):
    # first check if already valid
    if is_valid_sequence(arr):
        return True

    n = len(arr)
    for i in range(n):
        test_arr = arr[:i] + arr[i+1:]
        if is_valid_sequence(test_arr):
            return True

    return False


def part1():
    with open('input.txt') as f:
        reports = f.read().strip().split('\n')

    safe_report_count = 0 
    for report in reports:
        items = [int(i) for i in report.split(' ')]
        if is_valid_sequence(items):
            safe_report_count += 1

    print(safe_report_count)
        


def part2():
    with open('input.txt') as f:
        reports = f.read().strip().split('\n')

    single_bad = 0
    for report in reports:
        items = [int(i) for i in report.split(' ')]
        if tolerate_single_bad(items):
            single_bad += 1

    print(single_bad)






def main():
    # arg parser
    import argparse
    parser = argparse.ArgumentParser(description="Aoc Day2")

    parser.add_argument("--part1",action="store_true",help="Run part 1 of the day2")
    parser.add_argument("--part2",action="store_true",help="Run Part2 of the day2")

    args = parser.parse_args()

    if not(args.part1 or args.part2):
        print("Please provide flags")
        return

    if args.part1:
        part1()
    if args.part2:
        part2()
    


if __name__ == '__main__':
    main()
