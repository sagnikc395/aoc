class Directory:
    def __init__(self,currentPosn="/",nextPosn=""):
        self.currentPosn = currentPosn
        self.nextPosn = nextPosn
    
    def cd(self,next):
        pass

    def ls(self):
        pass

    def dirSize(self):
        pass 

    




def main():
    with open('temp.txt','r') as f:
        p= f.read().split('\n')
    print(p)


if __name__ == '__main__':
  main()
