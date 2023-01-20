def main():
    with open('input.txt','r') as f:
        p = [line.strip() for line in f]
    
    print(p)
    count = 0
    for password in p:
        items = password.split(" ")
        l1 = len(set(items))
        l2 = len(items)
        if(l1==l2):
            count+=1

    print(count)

main()
