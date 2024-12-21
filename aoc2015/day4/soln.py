import hashlib 

def min5_zeros(s):
    return len(s) >= 5 and s[:5] == "00000"

def min6_zeros(s):
    return len(s) >= 6 and s[:6] == "000000"


def part1():
    with open('./input.txt','r') as f:
        secret = f.read().strip()
    print(secret)
    
    index = 0 
    while True:
        res = secret + str(index)
        
        hashObj = hashlib.md5(res.encode())
        hexHash = hashObj.hexdigest() 
        
        if min5_zeros(hexHash):
            print(f"Solution : {hexHash},index: {index}")
            break 
        index += 1 

def part2():
    with open('./input.txt','r') as f:
        secret = f.read().strip()
    print(secret)
    
    index = 0 
    while True:
        res = secret + str(index)
        
        hashObj = hashlib.md5(res.encode())
        hexHash = hashObj.hexdigest() 
        
        if min6_zeros(hexHash):
            print(f"Solution : {hexHash},index: {index}")
            break 
        index += 1 


def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description='Aoc 2015, Day4')
    parser.add_argument('--part1',action='store_true',help='Run part1 solution')
    parser.add_argument('--part2',action='store_true',help='Run part2 solution')
    
    args = parser.parse_args()
    
    try:
        if args.part1:
            part1()
        elif args.part2:
            part2()
    except Exception as e:
        print("please use valid flags")
        
if __name__ == '__main__':
    main()