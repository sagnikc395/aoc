def smallestArea(l: int, w: int, h: int) -> int:
    a1 = l*w
    a2 = w*h
    a3 = h*l

    if (a1 < a2 and a1 < a3):
        return a1
    elif (a2 < a1 and a2 < a3):
        return a2
    elif (a3 < a2 and a3 < a1):
        return a3


def main():
    with open('input.txt', 'r') as f:
        p = f.read().split('\n')

    totalArea = 0
    for item in p:
        l, w, h = map(int, item.split('x'))
        totalArea += 2*l*w + 2*w*h + 2*l*h + smallestArea(l, w, h)

    print(totalArea)


main()
