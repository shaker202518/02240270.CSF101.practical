def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def sum_of_primes(start, end):
    try:
        start, end = int(start), int(end)
        if start > end:
            start, end = end, start
        return sum(n for n in range(start, end + 1) if is_prime(n))
    except ValueError:
        return "Invalid input: Please enter valid numbers"

def length_converter(value, unit):
    try:
        value = float(value)
        conversion_factors = {
            'M': (3.28084, 'feet'),    # meters to feet
            'CM': (0.0328084, 'feet'), # centimeters to feet
            'MM': (0.00328084, 'feet'),# millimeters to feet
            'KM': (3280.84, 'feet'),   # kilometers to feet
            'F': (0.3048, 'meters')    # feet to meters
        }
        
        unit = unit.upper()
        if unit not in conversion_factors:
            return "Invalid unit: Use M/F/CM/MM/KM"
        
        factor, target_unit = conversion_factors[unit]
        result = value * factor if unit == 'F' else value * factor
        return f"{round(result, 2)} {target_unit}"
    except ValueError:
        return "Invalid input: Please enter a valid number"

def count_consonants(text):
    if not isinstance(text, str):
        return "Invalid input: Please enter a valid string"
    consonants = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for c in text.lower() if c in consonants)

def min_max_finder(numbers):
    try:
        if not numbers:
            return "Empty input: Please enter some numbers"
        numbers = [float(n) for n in numbers]
        return min(numbers), max(numbers)
    except ValueError:
        return "Invalid input: Please enter valid numbers"

def palindrome_checker(text):
    if not isinstance(text, str):
        return "Invalid input: Please enter a valid string"
    text = ''.join(c.lower() for c in text if c.isalnum())
    return text == text[::-1]

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}")

def main():
    while True:
        print("\nMenu:")
        print("1. Sum of Prime Numbers")
        print("2. Length Converter")
        print("3. Count Consonants")
        print("4. Find Minimum and Maximum")
        print("5. Palindrome Checker")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            start = get_valid_input("Enter start number: ", int)
            end = get_valid_input("Enter end number: ", int)
            result = sum_of_primes(start, end)
            print(f"Sum of primes: {result}")
            
        elif choice == '2':
            value = get_valid_input("Enter value: ", float)
            unit = input("Enter unit (M/F/CM/MM/KM): ")
            result = length_converter(value, unit)
            print(f"Converted length: {result}")
            
        elif choice == '3':
            text = input("Enter a string: ")
            result = count_consonants(text)
            print(f"Number of consonants: {result}")
            
        elif choice == '4':
            numbers = input("Enter numbers (space-separated): ").split()
            result = min_max_finder(numbers)
            if isinstance(result, tuple):
                print(f"Smallest: {result[0]}, Largest: {result[1]}")
            else:
                print(result)
            
        elif choice == '5':
            text = input("Enter a string: ")
            result = palindrome_checker(text)
            print(f"Is palindrome: {result}")
            
        elif choice == '0':
            print("Thank you for using the program!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 0 and 5")
        
        if input("\nTry again? (y/n): ").lower() != 'y':
            print("Thank you for using the program!")
            break

if __name__ == "__main__":
    main()