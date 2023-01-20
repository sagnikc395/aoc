def main():
    with open('input.txt', 'r') as f:
        binary = f.read().split('\n')

    gammaRate = ""
    epsilonRate = ""

    for bi in binary:
        for bi2 in binary:
            print('{0:b}'.format(int(bi, 2) ^ int(bi2, 2)))


if __name__ == '__main__':
    main()
