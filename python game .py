import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Try again!")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

# Run the games
while True:
    print("\nChoose a game:")
    print("1. Guess the Number")
    print("2. Rock, Paper, Scissors")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        guess_the_number()
    elif choice == '2':
        rock_paper_scissors()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
