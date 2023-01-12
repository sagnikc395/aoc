def house_visited(directions):
    visited = 1
    visited_list = [[0, 0]]
    robo_coords = [0, 0]
    robo_coords = [0, 0]

    for char in directions:
        if char == "^":
            new_coords = [robo_coords[0], robo_coords[1]+1]
        elif char == "v":
            new_coords = [robo_coords[0], robo_coords[1]-1]
        elif char == "<":
            new_coords = [robo_coords[0]-1, robo_coords[1]]
        elif char == ">":
            new_coords = [robo_coords[0]+1, robo_coords[1]]

        if new_coords not in visited_list:
            visited_list.append(new_coords)
            visited += 1

        robo_coords = new_coords

    return visited


def main():
    with open('input.txt', 'r') as f:
        p = f.read()

    print(house_visited(p))


main()
