def part1():
    with open('./input.txt','r') as f:
        data = f.read().split('\n')
    data = [int(i) for i in data]
    
    result = 0 
    for item in result:
        result += item 
        
    print(result) 

def part2():
    with open('./input.txt','r') as f:
        data = f.read().split('\n')
    data = [int(i) for i in data]
    
    freqMap = {}
    curFreq = 0 
    found = False 
    
    while not found:
        for item in data:
            curFreq += item 
            
            if curFreq in freqMap:
                print(f"First freq reached twice: {curFreq}")
                found = True 
                break 
            freqMap[curFreq] = 1 
            
def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description="AoC 2018 Day1")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")
    
    args = parser.parse_args()
    
    if args.part1:
        part1()
    elif args.part2:
        part2()
    
    
if __name__ == '__main__':
    main()