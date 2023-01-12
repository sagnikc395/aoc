def main():
    with open("input.txt", "r") as f:
        p = f.readline()
    counter = 0
    for i in p:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
    print(counter)


if __name__ == '__main__':
    main()
