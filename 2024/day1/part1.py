def main():
    with open('input.txt','r') as f:
        p = f.read().strip()

    lines = p.split('\n')
    ll = []
    rr = []

    for line in lines:
        l,r = map(int,line.split())
        ll.append(l)
        rr.append(r)

    ll = sorted(ll)
    rr = sorted(rr)

    ans = 0
    for l,r in zip(ll,rr):
        ans += abs(l-r)

    print(ans)


if __name__ == '__main__':
    main()
