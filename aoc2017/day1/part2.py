def main():
    with open('input.txt','r') as f:
        p=f.read().strip()
    
        ds = [int(d) for d in p]
        n=len(ds)

        su=0
        for i,d in enumerate(ds):
            if d == ds[(i+n//2)%n]:
                su+=d
        print(su)


if __name__ == '__main__':
    main()
