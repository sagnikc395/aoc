def count_trees_multiple_slopes():
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

    # Define slopes to check
    slopes = [
        {'dx': 1, 'dy': 1},
        {'dx': 3, 'dy': 1},
        {'dx': 5, 'dy': 1},
        {'dx': 7, 'dy': 1},
        {'dx': 1, 'dy': 2},
    ]

    result = 1  # Initialize to 1 for multiplication

    # Check each slope
    for slope in slopes:
        tree_count = 0
        x = 0
        y = 0

        # Traverse the slope
        while y < height:
            # Handle wrapping around using modulo
            current_x = x % width
            current_line = data[y]

            # Check for tree
            if current_line[current_x] == '#':
                tree_count += 1

            # Move position according to slope
            x += slope['dx']
            y += slope['dy']

        result *= tree_count

    print(result)

if __name__ == "__main__":
    count_trees_multiple_slopes()