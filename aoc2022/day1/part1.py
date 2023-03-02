

def main():
    with open('input.txt', 'r') as f:
        elves = f.read().split('\n\n')
    res = [list(map(int, elf.strip().split("\n"))) for elf in elves]
    current_max = 0
    for elf in res:
        if current_max <= sum(elf):
            current_max = sum(elf)
    print(current_max)


if __name__ == '__main__':
    main()
