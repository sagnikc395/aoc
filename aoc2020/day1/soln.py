def part1():
    with open('./input.txt','r') as f:
        contents = f.read().strip('').split('\n')
    
    seen = set() 
    for num in contents:
        complement = 2020 - int(num)
        if complement in seen:
            print(f"{complement} {num}")
        seen.add(num)
    
def three_sum(numbers):
    
    numbers = sorted(numbers)
    target = 2020
    
    for i,num in enumerate(numbers):
        left = i + 1 
        right = len(numbers) - 1
        remaining = target  - int(num)
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == remaining:
                print(f"{num} {numbers[left]} {numbers[right]}")
                break 
            elif current_sum < remaining:
                left+=1
            else:
                right -=1
         
def part2():
    with open('./input.txt','r') as f:
        contents = f.read().strip().split('\n')
        
    three_sum(contents)
     

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="AoC 2020 , Day1")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")
    
    
    args = parser.parse_args()
    
    if args.part1:
        part1()
    elif args.part2:
        part2()
        
if __name__ == '__main__':
    main()