import re

def threeOrMoreVowels(inputstr):
    vowels = ['a','e','i','o','u']
    count = 0

    for index,val in enumerate(vowels):
        count += inputstr.count(val)

    if count >=3:
        return  True
    else:
        return False


def repeatingLetter(inputStr):
    for i in range(len(inputStr)-1):
        if inputStr[i] == inputStr[i+1]:
            return True

    return False

def excludeBadSubStrings(inputStr):
    return re.search("ab|cd|pq|xy",inputStr) 


def allowedString(inputStr):
    if threeOrMoreVowels(inputStr) and repeatingLetter(inputStr) and excludeBadSubStrings(inputStr):
        return True
    else:
        return False 


def main():
    with open('input.txt','r') as f:
        p=f.readlines()

    p=[line.split() for line in p]
    #print(p)
    count= 0 
    for lines in enumerate(p):
        if allowedString(lines):
            count+=1

    print(count)


main()
