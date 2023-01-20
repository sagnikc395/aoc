def main():

    with open('input.txt', 'r') as f:
        p = [line.strip() for line in f]

    #print(p)

    # p = ["abcde xyz ecdab", "abcde fghij","oiii ioii iioi iiio","a ab abc abd abf abj"]
    invalid = 0
    for password in p:
        items = password.split(" ")
        l1 = len(set(items))
        l2 = len(items)
        if(l1==l2):
            invalid+=1
        items = [''.join(sorted(item)) for item in items]
        print(items)
        if (len(set(items)) != 1):
            invalid += 1

    print(invalid)


main()
