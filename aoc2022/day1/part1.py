def main():
    with open('input.txt','r') as f:
        p= [line.strip() for line in f]

    #print(p)
    calories=[]
    summ=0
    
    for item in p:
        if item != '':
            summ +=int(item)
        else:
            calories.append(summ)
            summ=0
    
    print(calories)
    calories.sort(reverse=True)
    print(calories[0])




if __name__=='__main__':
    main()
