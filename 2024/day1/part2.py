
from collections import defaultdict ,Counter


def main():
    with open('input.txt','r') as f:
        p = f.read().strip()

    lines = p.split('\n')
    ll = []
    rc = Counter()

    for line in lines:
        l,r = map(int,line.split())
        ll.append(l)
        rc[r] += 1

    ll = sorted(ll)
   # rr = sorted(rr)

    ans = 0

    for l in ll:
        ans += l * rc.get(l,0)


    print(ans)


if __name__ == '__main__':
    main()
