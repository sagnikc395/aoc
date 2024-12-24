import re

def is_tls(ip: str) -> bool:
    # Helper function to check for ABBA pattern
    def has_abba(text: str) -> bool:
        for i in range(len(text) - 3):
            a, b, c, d = text[i:i+4]
            if a == d and b == c and a != b:
                return True
        return False

    # Check outside brackets
    # Split the string at brackets and take even-indexed parts (outside brackets)
    outside_parts = re.split(r'\[.*?\]', ip)
    if not any(has_abba(part) for part in outside_parts):
        return False

    # Check inside brackets
    # Find all text within brackets
    inside_parts = re.findall(r'\[(.*?)\]', ip)
    if any(has_abba(part) for part in inside_parts):
        return False

    return True

def main():
    with open("input.txt", "r") as file:
        data = file.read().strip()

    # Count IPs that support TLS
    count = sum(1 for ip in data.splitlines() if is_tls(ip))
    print(count)

if __name__ == "__main__":
    main()
