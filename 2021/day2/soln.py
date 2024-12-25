class Position:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.aim = 0

    def forward(self,f):
        self.x += f
        self.y += ( self.aim * f)

    def down(self,d):
        #self.y += d
        self.aim += d

    def up(self,u):
        #self.y -= u
        self.aim -= u


def part1():
    with open('./input.txt','r') as f:
        cmds = f.read().strip().split('\n')

    point = Position(0,0)
    for cmd in cmds:
        current_posn,val = cmd.split(" ")
        if current_posn == "forward":
            point.forward(int(val))
        elif current_posn == "down":
            point.down(int(val))
        elif current_posn == "up":
            point.up(int(val))

    print(point.x * point.y)

def part2():
    with open('./input.txt','r') as f:
        cmds= f.read().strip().split('\n')

    point = Position(0,0)
    for cmd in cmds:
        command,val = cmd.split(" ")
        if command == "forward":
            point.forward(int(val))
        elif command == "down":
            point.down(int(val))
        elif command == "up":
            point.up(int(val))


    print(point.x * point.y)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="AoC Day 2021 Day2")
    parser.add_argument("--part1",action="store_true",help="Solve Part1")
    parser.add_argument("--part2",action="store_true",help="Solve Part2")

    args = parser.parse_args()

    if args.part1:
        part1()
    elif args.part2:
        part2()

if __name__ == '__main__':
    main()
