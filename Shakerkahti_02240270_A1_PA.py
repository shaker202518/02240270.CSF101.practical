def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def sum_of_primes(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):
    return round(value * 3.28084, 2) if unit.upper() == 'M' else round(value / 3.28084, 2) if unit.upper() == 'F' else "Invalid unit"

def count_consonants(text):
    return sum(1 for c in text.lower() if c in "bcdfghjklmnpqrstvwxyz")

def min_max_finder(numbers):
    return min(numbers), max(numbers) if numbers else "Invalid input"

def palindrome_checker(text):
    t = text.lower().replace(" ", "")
    return t == t[::-1]

def main():
    while True:
        choice = input("\n1. Sum primes\n2. Convert length\n3. Count consonants\n4. Min/Max\n5. Palindrome\n0. Exit\n> ")
        
        if choice == '1':
            start, end = int(input("Start: ")), int(input("End: "))
            print("Sum of primes:", sum_of_primes(start, end))
        elif choice == '2':
            value, unit = float(input("Value: ")), input("Unit (M/F): ")
            print("Converted length:", length_converter(value, unit))
        elif choice == '3':
            print("Number of consonants:", count_consonants(input("String: ")))
        elif choice == '4':
            numbers = list(map(int, input("Numbers (space-separated): ").split()))
            min_val, max_val = min_max_finder(numbers)
            print(f"Smallest: {min_val}, Largest: {max_val}")
        elif choice == '5':
            print("Is palindrome:", palindrome_checker(input("String: ")))
        elif choice == '0':
            break
        else:
            print("Invalid choice")
        
        if input("Try again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
