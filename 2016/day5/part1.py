import hashlib

def find_password(door_id: str) -> str:
    password = ""
    index = 0

    while len(password) < 8:
        # Create string to hash and encode to bytes
        to_hash = f"{door_id}{index}".encode()

        # Calculate MD5 hash and convert to hexadecimal
        hash_result = hashlib.md5(to_hash).hexdigest()

        # Check if hash starts with five zeros
        if hash_result.startswith("00000"):
            password += hash_result[5]
            print(f"Found character {len(password)}: {hash_result[5]}")  # Progress indicator

        index += 1

    return password

def main():
    input_id = "uqwqemis"
    password = find_password(input_id)
    print(f"The password is: {password}")

if __name__ == "__main__":
    main()
