def main():
    with open('input.txt', 'r') as f:
        p = f.read().split("\n\n")
    res = [list(map(int, elf.strip().split("\n"))) for elf in p]

    summed_calories = [sum(elf) for elf in res]
    print(sum(sorted(summed_calories, reverse=True)[0:3]))


if __name__ == '__main__':
    main()
