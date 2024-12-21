import math 


def part1():
    with open('./input.txt','r') as f:
        data = f.read().split('\n')
    data = [int(m) for m in data]
    
    fuel_req = 0 
    for fuel in data:
        curr_fuel_req = math.floor(fuel // 3) - 2
        fuel_req += curr_fuel_req
        
    print(fuel_req)

def part2():
    pass 



def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description="AoC 2019, Day1")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")
    
    args = parser.parse_args()
    
    if args.part1:
        part1()
    elif args.part2:
        part2()


if __name__ == '__main__':
    main()
    