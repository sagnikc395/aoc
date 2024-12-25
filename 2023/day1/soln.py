digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
def find_calibration(input_text: str) -> int:
    # Split input into lines
    lines = input_text.splitlines()
    total_sum = 0
    
    for line in lines:
        # Ignore empty or whitespace-only lines
        if line.strip():
            # Split the line into words based on non-word characters
            words = line.split()
            
            # Find the first and last digits in the words
            first_digit = next((digits[word] for word in words if word in digits), 0)
            last_digit = next((digits[word] for word in reversed(words) if word in digits), 0)
            
            # Calculate the calibration value (first_digit * 10 + last_digit)
            calibration_value = first_digit * 10 + last_digit
            total_sum += calibration_value
    
    return total_sum


def part1():
    
    with open('./input.txt', 'r') as file:
        items = file.read().splitlines()
    
    result = 0
    for item in items:
        # Find first digit
        first_digit = next((int(char) for char in item if char.isdigit()), 0)
        
        # Find last digit
        last_digit = next((int(char) for char in reversed(item) if char.isdigit()), 0)
        
        cal_value = first_digit * 10 + last_digit
        result += cal_value
    
    print(result)

def part2():
    with open("./input.txt", "r") as file:
        items = file.read()
    
    # Get the sum from the find_calibration function
    sum_value = find_calibration(items)
    
    # Print the result
    print(sum_value)



def main():
    import argparse 
    
    parser = argparse.ArgumentParser(description="AoC 2023 Day1")
    parser.add_argument("--part1",action="store_true",help="solve part1")
    parser.add_argument("--part2",action="store_true",help="solve part2")
    
    args = parser.parse_args()
    
    if args.part1:
        part1()
    elif args.part2:
        part2()
        
if __name__ == '__main__':
    main()