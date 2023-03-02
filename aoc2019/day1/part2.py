import math


def calculateFuel(input):
    return math.floor(float(input)//3)-2


def main():
    with open('input.txt', 'r') as f:
        p = [int(i.strip()) for i in f]
    totalFuel = 0
    for item in p:
        temp = calculateFuel(item)
        while(temp>0):
            totalFuel += temp
            temp = calculateFuel(temp)
    print(totalFuel)


main()
