def main():
    with open('input.txt', 'r') as f:
        commands = f.read().split('\n')

    h = 0
    v = 0
    aim = 0

    for command in commands:
        direc, val = command.split(" ")
        val = int(val)
        if direc == "forward":
            h += val
            v += aim * val
        elif direc == "down":
            aim += val
        elif direc == "up":
            aim -= val

    print(h*v)


if __name__ == '__main__':
    main()
