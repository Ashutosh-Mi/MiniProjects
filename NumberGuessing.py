from random import randint

def number_guessing_game():
    print("Welcome to the Guessing game!")
    
    while True:  # Keep the game running until the user decides to quit
        number = randint(1, 100)
        guesses = 0
        
        while True:
            try:
                guess = int(input("Enter the number between 1 and 100: "))
                
                # Validate the guess
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                guesses += 1
                if guess < number:
                    print("Enter a higher number. Try again.")
                elif guess > number:
                    print("Enter a lower number. Try again.")
                else:
                    print(f"You guessed the correct number {number} in {guesses} guesses!")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 100.")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Calling the game function
number_guessing_game()
