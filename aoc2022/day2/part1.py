def main():

    with open('input.txt','r') as f:
        data = [line.strip() for line in f]


    score = 0

    for item in data:
        oppn,user = item.split(' ')
        if(oppn=='A'):#rock
            if(user=='X'):
                score+=4
            elif(user=='Y'):
                score+=8
            elif(user=='Z'):
                score+=3
        elif(oppn=='B'):#paper
            if(user=='X'):
                score+=1
            elif(user=='Y'):
                score+=5
            elif(user=='Z'):
                score+=9
        elif(oppn=='C'):#scissor
            if(user=='X'):
                score+=7
            elif(user=='Y'):
                score+=2
            elif(user=='Z'):
                score+=6

    
    print(score)


if __name__=='__main__':
    main()
