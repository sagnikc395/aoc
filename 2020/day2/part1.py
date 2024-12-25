def validate_passwords():
    try:
        with open('./input.txt', 'r') as file:
            items = file.read().splitlines()
    except FileNotFoundError:
        print("Error: input.txt file not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    count = 0
    for password_line in items:
        # Skip empty lines
        if not password_line:
            continue
            
        # Split into policy and password
        parts = password_line.split(":")
        if len(parts) != 2:
            continue

        policy, password = parts
        
        # Parse policy
        policy_parts = policy.split()
        if len(policy_parts) != 2:
            continue
            
        range_str, key = policy_parts
        
        # Parse range
        range_parts = range_str.split("-")
        if len(range_parts) != 2:
            continue
            
        try:
            low, upper = map(int, range_parts)
        except ValueError:
            continue

        # Count character occurrences
        password = password.strip()
        char_count = password.count(key)
        
        # Check if password meets policy
        if low <= char_count <= upper:
            count += 1

    print(count)

if __name__ == "__main__":
   validate_passwords()