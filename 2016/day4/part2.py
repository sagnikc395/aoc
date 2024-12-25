import re
from typing import Optional

def decrypt_name(encrypted_name: str, sector_id: int) -> str:
    shift = sector_id % 26
    decrypted = []

    for char in encrypted_name:
        if char == '-':
            decrypted.append(' ')
        elif 'a' <= char <= 'z':
            # Calculate new character code with shift
            new_char_code = ((ord(char) - ord('a') + shift) % 26) + ord('a')
            decrypted.append(chr(new_char_code))
        else:
            decrypted.append(char)

    return ''.join(decrypted)

def find_north_pole_sector_id(rooms: list[str]) -> Optional[int]:
    pattern = r'^([a-z-]+)-(\d+)\[([a-z]+)\]$'

    for room in rooms:
        match = re.match(pattern, room)
        if not match:
            continue

        name, sector_id_str, _ = match.groups()
        sector_id = int(sector_id_str)
        decrypted_name = decrypt_name(name, sector_id)

        if 'northpole' in decrypted_name:
            return sector_id

    return None

def main():
    with open("input.txt", "r") as file:
        items = file.read().splitlines()

    north_pole_sec_id = find_north_pole_sector_id(items)

    if north_pole_sec_id is not None:
        print(f"Sector ID of the room: {north_pole_sec_id}")
    else:
        print("No room with 'northpole' found.")

if __name__ == "__main__":
    main()
