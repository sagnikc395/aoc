import hashlib

def find_password_with_position(door_id: str) -> str:
    password = ["_"] * 8  # Initialize with 8 underscores
    index = 0
    filled_positions = 0

    while filled_positions < 8:
        # Create string to hash and encode to bytes
        to_hash = f"{door_id}{index}".encode()

        # Calculate MD5 hash and convert to hexadecimal
        hash_result = hashlib.md5(to_hash).hexdigest()

        # Check if hash starts with five zeros
        if hash_result.startswith("00000"):
            # Try to get position from the 6th character
            try:
                position = int(hash_result[5])
                if position < 8 and password[position] == "_":
                    password[position] = hash_result[6]
                    filled_positions += 1
                    # Print current state of password
                    print(f"Found position {position}: {''.join(password)}")
            except ValueError:
                # Skip if 6th character isn't a valid number
                pass

        index += 1

    return "".join(password)

def main():
    door_id = "uqwqemis"
    password = find_password_with_position(door_id)
    print(f"The password is: {password}")

if __name__ == "__main__":
    main()
