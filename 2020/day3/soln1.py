def count_trees():
    try:
        with open('./input.txt', 'r') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        print("Error: input.txt file not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Get dimensions of the map
    width = len(data[0]) if data else 0
    height = len(data)

    # Initialize counters
    tree_count = 0
    x = 0
    y = 0

    # Traverse the slope (right 3, down 1)
    while y < height:
        # Handle wrapping around using modulo
        current_x = x % width
        current_line = data[y]

        # Check for tree
        if current_line[current_x] == '#':
            tree_count += 1

        # Move position
        x += 3  # Move right 3
        y += 1  # Move down 1

    print(tree_count)

if __name__ == "__main__":
    count_trees()