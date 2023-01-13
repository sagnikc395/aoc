

def main():
    with open('input.txt', 'r') as p:
        f = p.read().split('\n')

    currentF = 0
    for item in f:
        if '+' in item:
            currentF += int(item[1:])
        elif '-' in item:
            currentF -= int(item[1:])

    print(currentF)


if __name__ == '__main__':
    main()
