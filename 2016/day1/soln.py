

DIRECTIONS = ["N","E",'W','S']

def manhattan(a,b):
    distance = 0 
    dimension = max(len(a),len(b))
    for i in range(0,dimension):
        distance += abs((b[i] or 0) - (a[i] or 0))
    return distance
    
def part1():
    def move_north(v): coords[1] += v 
    def move_east(v): coords[0] += v 
    def move_south(v): coords[1] -= v 
    def move_west(v): coords[0] -= v 
    
    move = {
        'N': move_north,
        'E': move_east,
        'S': move_south,
        'W': move_west
    }
    
    def rotate(curr, current_dir):
        if curr == 'R':
            return (current_dir + 1) % len(DIRECTIONS)
        else:  # L
            return (current_dir - 1) % len(DIRECTIONS)
    
    # Initialize variables
    coords = [0, 0]
    current_dir = 0  # Start facing North
    
    # Read and parse input
    with open('./input.txt', 'r') as f:
        contents = f.read().strip()
    movements = [m.strip() for m in contents.split(",")]
    
    # Process movements
    for mvmt in movements:
        turn = mvmt[0]
        walk = int(mvmt[1:], 10)
        
        # Update direction and move
        current_dir = rotate(turn, current_dir)
        facing = DIRECTIONS[current_dir]
        move[facing](walk)
    
    # Calculate and print result
    print(manhattan([0, 0], coords))
       
def part2():
    with open('./input.txt','r') as f:
        contents = f.read().strip()
    
    movements = [m.strip() for m in contents.split(",")]
    move = {
        'N': lambda v: (0, v),
        'E': lambda v: (v, 0),
        'S': lambda v: (0, -v),
        'W': lambda v: (-v, 0)
    }
    
    def check_and_add_position(x, y, visited_positions, first_repeat):
        pos_key = f"{x},{y}"
        if pos_key in visited_positions and first_repeat is None:
            first_repeat = [x, y]
        visited_positions.add(pos_key)
        return first_repeat
    
    # Initialize variables
    curr_direction = 0
    coords = [0, 0]
    visited_positions = {"0,0"}
    first_repeat = None
    
    def rotate(curr):
        nonlocal curr_direction
        if curr == "R":
            curr_direction = (curr_direction + 1) % len(DIRECTIONS)
        else:
            curr_direction = (curr_direction + 3) % len(DIRECTIONS)
    
    # Read input
    with open('./input.txt', 'r') as f:
        contents = f.read().strip()
    movements = [m.strip() for m in contents.split(",")]
    
    # Process movements
    for movement in movements:
        if first_repeat:
            break
            
        turn = movement[0]
        walk = int(movement[1:], 10)
        
        rotate(turn)
        facing = DIRECTIONS[curr_direction]
        dx, dy = move[facing](walk)
        
        # Move one step at a time and check each position
        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0
        
        # Handle x movement
        for _ in range(abs(dx)):
            coords[0] += step_x
            first_repeat = check_and_add_position(coords[0], coords[1], 
                                                visited_positions, first_repeat)
            if first_repeat:
                break
                
        if first_repeat:
            break
            
        # Handle y movement
        for _ in range(abs(dy)):
            coords[1] += step_y
            first_repeat = check_and_add_position(coords[0], coords[1], 
                                                visited_positions, first_repeat)
            if first_repeat:
                break
    
    # Print results
    if first_repeat:
        print(f"First location visited twice: {first_repeat}")
        print(f"Distance to first repeat: {manhattan([0, 0], first_repeat)}")
    print(f"Final distance: {manhattan([0, 0], coords)}")

def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description='Aoc 2016, Day1')
    parser.add_argument('--part1',action='store_true',help='Run part1 solution')
    parser.add_argument('--part2',action='store_true',help='Run part2 solution')
    
    args = parser.parse_args()
    
   
    if args.part1:
        part1()
    elif args.part2:
        part2()
        
if __name__ == '__main__':
    main()