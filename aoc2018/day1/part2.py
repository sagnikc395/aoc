
from itertools import cycle

def main():
    with open('input.txt', 'r') as p:
        f = p.read().split('\n')

    currentF = 0
    freqList=[]
    pool = cycle(f)
    for item in pool:
        if '+' in item:
            currentF += int(item[1:])
            if currentF in freqList:
                print(currentF)
                break 
            else:
                freqList.append(currentF)
        elif '-' in item:
            currentF -= int(item[1:])
            if currentF in freqList:
                print(currentF)
                break 
            else:
                freqList.append(currentF)

if __name__ == '__main__':
    main()
