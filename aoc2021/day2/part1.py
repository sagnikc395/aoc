def main():
    with open('input.txt', 'r') as f:
        commands = f.read().split('\n')

    h = 0
    v = 0

    for command in commands:
        direc, val = command.split(" ")
        val = int(val)
        if direc == "forward":
            h += val
        elif direc == "down":
            v += val
        elif direc == "up":
            v -= val

    print(h*v)


if __name__ == '__main__':
    main()
