import string 



def main():

    with open('input.txt','r') as f:
        p = [line.strip() for line in f]
    
    pri_sum = 0
    pri = string.ascii_lowercase + string.ascii_uppercase
    
    elf = 0
    badge = None
    #common_items=[]
    for item in p:
        size = len(item) // 2
        first = set(item[:size])
        second = set(item[size:])

        #common_items.append(''.join(set(first).intersection(second)))
        #pri_sum += pri.index((first & second).pop()) +1
        
        if elf %3==0:
            badge = set(item)

        badge &= set(item)

        if len(badge) == 1:
            pri_sum += pri.index(badge.pop())+1

        elf +=1

    #print(common_items)
    # for priorities
    #priority = []
    '''
    for item in common_items:
        if ord(item) > 97 and ord(item)<122:
            priority.append(ord(item)-96)
        elif ord(item)>64 and ord(item)<91:
            priority.append(ord(item)-38)
    '''
    #print(priority)
    #print(sum(priority))
    
    print(pri_sum)


if __name__ == '__main__':
    main()


