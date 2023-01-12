def repeatingLetterGap(inputStr):
    for i in range(len(inputStr)-2):
        if inputStr[i] == inputStr[i+2]:
            return True
    return False


def twoPairs(inputStr):
    for i in range(len(inputStr)-2):
        if inputStr.count(inputStr[i:i+2])>=2:
            return True

    return False


def main():
    with open("input.txt", "r") as f:
        p = f.readlines()
    p = [line.strip() for line in p]

    #print(p)
        
    count = 0

    for line in p:
        if repeatingLetterGap(line) and twoPairs(line):
            count+=1

    print(count)

main()
