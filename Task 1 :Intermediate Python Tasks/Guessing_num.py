import random

# Custom Exception
class InvalidInputError(Exception):
    def __init__(self, mes="Invalid input! Please enter an integer between 1 and 10."):
        self.mes = mes
        super().__init__(self.mes)

# Random Number Generation
def secret_number():
    return random.randint(1, 10)

# User Input Validation
def validate_input(user_input):
    try:
        num = int(user_input)
        if num < 1 or num > 10:
            raise InvalidInputError("The number must be between 1 and 10.")
        return num
    except ValueError:
        raise InvalidInputError("Please enter a valid integer.")

# Main Function
def play_game():
    secret_num = secret_number()
    score = 50
    attempts = 5  
    print("Welcome to the Game!")
    print("The secret number is between 1 and 10. Can you guess it?")
    
    while attempts > 0:
        try:
            user_guess = input(f" \nAttempts left: {attempts} \nEnter your guess (1-10) | : ")
            validated_guess = validate_input(user_guess)
            
            # Check if the guess is correct
            if validated_guess == secret_num:
                print(f"Congratulations! You guessed the correct number {secret_num}")
                print(f"Your final score is: {score}")
                break
            else:
                score -= 10
                attempts -= 1  
                
                if attempts == 0:
                    print("Sorry, you've used all your attempts. Better luck next time!")
                    print(f"The secret number was: {secret_num}")
                    break
                
                print("Wrong guess! Try again.")
                print(f"Current score: {score}")
        except InvalidInputError as e:
            print(e)

    # Ask the user if they want to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            play_game()  
            break
        elif play_again == "no":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()
