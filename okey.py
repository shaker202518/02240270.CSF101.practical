def print_separator():
    print("\n" + "="*50 + "\n")

def print_result(title, result):
    print_separator()
    print(f"{title}:")
    print(f"Result: {result}")
    print_separator()

def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def sum_of_primes(start, end):
    try:
        start, end = int(start), int(end)
        if start > end:
            start, end = end, start
        prime_numbers = [n for n in range(start, end + 1) if is_prime(n)]
        total = sum(prime_numbers)
        return f"Sum: {total}\nPrime numbers found: {prime_numbers}"
    except ValueError:
        return "Invalid input: Please enter valid numbers"

def length_converter(value, unit):
    try:
        value = float(value)
        conversion_factors = {
            'M': (3.28084, 'feet', 'meters'),
            'CM': (0.0328084, 'feet', 'centimeters'),
            'MM': (0.00328084, 'feet', 'millimeters'),
            'KM': (3280.84, 'feet', 'kilometers'),
            'F': (0.3048, 'meters', 'feet')
        }
        
        unit = unit.upper()
        if unit not in conversion_factors:
            return "Invalid unit: Use M/F/CM/MM/KM"
        
        factor, target_unit, source_unit = conversion_factors[unit]
        result = value * factor if unit == 'F' else value * factor
        return f"{value} {source_unit} = {round(result, 2)} {target_unit}"
    except ValueError:
        return "Invalid input: Please enter a valid number"

def count_consonants(text):
    if not isinstance(text, str):
        return "Invalid input: Please enter a valid string"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = sum(1 for c in text.lower() if c in consonants)
    consonants_found = [c for c in text.lower() if c in consonants]
    return f"Count: {count}\nConsonants found: {', '.join(sorted(set(consonants_found)))}"

def min_max_finder(numbers):
    try:
        if not numbers:
            return "Empty input: Please enter some numbers"
        numbers = [float(n) for n in numbers]
        return f"Smallest: {min(numbers)}\nLargest: {max(numbers)}\nNumbers analyzed: {numbers}"
    except ValueError:
        return "Invalid input: Please enter valid numbers"

def palindrome_checker(text):
    if not isinstance(text, str):
        return "Invalid input: Please enter a valid string"
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    is_palindrome = cleaned_text == cleaned_text[::-1]
    return f"Original text: {text}\nCleaned text: {cleaned_text}\nIs palindrome: {is_palindrome}"

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            value = input_type(input(prompt))
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}")

def display_menu():
    print("\n" + "*"*20 + " MENU " + "*"*20)
    print("1. Sum of Prime Numbers")
    print("2. Length Converter")
    print("3. Count Consonants")
    print("4. Find Minimum and Maximum")
    print("5. Palindrome Checker")
    print("0. Exit")
    print("*"*46 + "\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            start = get_valid_input("Enter start number: ", int)
            end = get_valid_input("Enter end number: ", int)
            print_result("Prime Numbers Analysis", sum_of_primes(start, end))
            
        elif choice == '2':
            value = get_valid_input("Enter value: ", float)
            unit = input("Enter unit (M/F/CM/MM/KM): ")
            print_result("Length Conversion", length_converter(value, unit))
            
        elif choice == '3':
            text = input("Enter a string: ")
            print_result("Consonants Analysis", count_consonants(text))
            
        elif choice == '4':
            numbers = input("Enter numbers (space-separated): ").split()
            print_result("Number Analysis", min_max_finder(numbers))
            
        elif choice == '5':
            text = input("Enter a string: ")
            print_result("Palindrome Analysis", palindrome_checker(text))
            
        elif choice == '0':
            print("\nThank you for using the program!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 0 and 5")
        
        if input("\nWould you like to try another operation? (y/n): ").lower() != 'y':
            print("\nThank you for using the program!")
            break

if __name__ == "__main__":
    print("\nWelcome to the Utility Functions Program!")
    main()