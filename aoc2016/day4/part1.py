import re
from collections import Counter

def is_real_room(name: str, checksum: str) -> bool:
    # Remove dashes and count letter frequencies using Counter
    letter_counts = Counter(name.replace('-', ''))

    # Sort letters by frequency (descending) and then alphabetically
    sorted_letters = sorted(
        letter_counts.keys(),
        key=lambda x: (-letter_counts[x], x)
    )

    # Generate the checksum from the five most common letters
    generated_checksum = ''.join(sorted_letters[:5])
    return generated_checksum == checksum

def sum_of_real_room_sector_ids(rooms: list[str]) -> int:
    sum_ids = 0
    pattern = r'^([a-z-]+)-(\d+)\[([a-z]+)\]$'

    for room in rooms:
        match = re.match(pattern, room)
        if not match:
            continue

        name, sector_id, checksum = match.groups()
        if is_real_room(name, checksum):
            sum_ids += int(sector_id)

    return sum_ids

def main():
    with open("input.txt", "r") as file:
        items = file.read().splitlines()

    total_sector_id_sum = sum_of_real_room_sector_ids(items)
    print(f"Sum of sector IDs for real rooms: {total_sector_id_sum}")

if __name__ == "__main__":
    main()
