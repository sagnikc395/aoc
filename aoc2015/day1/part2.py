def main():
    with open("input.txt", "r") as f:
        p = f.readline()
    counter = 0
    posn = 0
    for i in p:
        if counter == -1:
            break
        else:
            if i == '(':
                counter += 1
            elif i == ')':
                counter -= 1
            posn += 1
    print(posn)


if __name__ == '__main__':
    main()
