def validate_passwords():
    try:
        with open('./input.txt', 'r') as file:
            data = file.read().splitlines()
    except FileNotFoundError:
        print("Error: input.txt file not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    count = 0
    for password_line in data:
        # Skip empty lines
        if not password_line:
            continue
            
        # Split into policy and password
        try:
            policy, password = password_line.split(":")
            password = password.strip()  # Remove leading/trailing whitespace
            
            # Parse policy
            lower_str, rest = policy.split("-")
            upper_str, key = rest.split()
            
            # Convert positions to integers
            pos1, pos2 = int(lower_str), int(upper_str)
            
            # Check if exactly one position matches
            # Note: Subtract 1 from positions since policy uses 1-based indexing
            is_valid = (password[pos1 - 1] == key) != (password[pos2 - 1] == key)
            
            if is_valid:
                count += 1
                
        except (ValueError, IndexError):
            # Skip malformed lines
            continue

    print(count)

if __name__ == "__main__":
    validate_passwords()