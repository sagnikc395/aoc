
def main():
    with open('input.txt', 'r') as f:
        p = f.read().split('\n')
    p = map(lambda x: int(x), p)
    p = list(p)
    counter = 0

    for i in range(1, len(p)):
        if p[i] > p[i-1]:
            counter += 1
    print(counter)

if __name__ == '__main__':
    main()
