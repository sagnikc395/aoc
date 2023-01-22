class Computer:
    def __init__(self):
        self.X = 1
        self.cycle = 0

    def solve(self,items):
        res = 0
        while(self.cycle!=221):
            for item in items:
                if(item=="noop"):
                    self.cycle+=1
                else:
                    oper,val = item.split(" ")
                    self.X += int(val)
                    self.cycle+=2
                print(self.cycle)


def main():
    with open('input.txt','r') as f:
        items=f.read().split('\n')
    
    calc = Computer()
    print(calc.solve(items))


if __name__ =='__main__':
    main()
