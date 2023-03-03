from enum import Enum , auto

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def beats(self):
        if(self==Move.ROCK):
            return Move.SCISSORS
        elif(self==Move.PAPER):
            return Move.PAPER
        elif(self==Move.SCISSORS):
            return Move.PAPER


    def loses_by(self):
        if(self==Move.ROCK):
            return Move.PAPER
        elif(self==Move.PAPER):
            return Move.SCISSORS
        elif(self==Move.SCISSORS):
            return Move.ROCK

    def move_score(self) ->int:
        if(self==Move.ROCK):
            return 1
        elif(self==Move.PAPER):
            return 2
        elif(self==Move.SCISSORS):
            return 3
        else:
            raise ValueError("Invalid Move")

    @classmethod
    def to_move(cls,move:str):
        if(move== "A" or move == "X"):
            return Move.ROCK
        elif(move=="B" or move== "Y"):
            return move.PAPER
        elif(move=="C" or move== "Z"):
            return Move.SCISSORS
        else:
            raise ValueError("Invalid move")

        
def calc_outcome_score(opp_move,my_move: Move) -> int:
    if opp_move == my_move:
        # draw
        return 3
    if my_move == opp_move.loses_by():
        # win 
        return 6

    if my_move == oop_move.beats():
        #lose
        return 0

    raise ValueError("Invalid Moves")
    
def main():
    with open('input.txt','r') as f:
        p = [tuple(line.split()) for line in f.readlines()]

    total_score = 0
    for move in p:
        oop , my = Move.to_move(move[0]),Move.to_move(move[1])
        total_score += my.move_score()
        total_score += calc_outcome_score(oop,my)

    print(total_score)

if __name__ == '__main__':
    main()
