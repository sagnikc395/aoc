import math


def main():
    with open('input.txt', 'r') as f:
        p = [int(i.strip()) for i in f]
    # print(p)
    fuelRequired = 0
    for item in p:
        item = math.floor(float(item)//3)
        item = item - 2
        fuelRequired += item
    print(fuelRequired)


main()
