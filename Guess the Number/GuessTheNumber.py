import random
import time
def generate_secret_number():
    l=[0,1,2,3,4,5,6,7,8,9]
    secret_number = str(random.choice([1,2,3,4,5,6,7,8,9]))
    l.pop(l.index(int(secret_number)))
    while len(secret_number) < 5:
        digit = random.choice(l)
        l.pop(l.index(digit))
        secret_number += str(digit)
    return secret_number
def main():
    print("welcome to the game find the 5 digit number!")
    print("you have 10 chances to guess the number")
    print("the number is between 10000 and 99999")
    print("No repeated digits are allowed")
    print("you will be given hints after each guess")
    print("if you guess a digit in the correct position, you will get a '+'")
    print("if you guess a digit in the wrong position, you will get a '-'") 
    print("if you guess a digit that is not in the number, you will get a '*'")
    print("Time will start after you enter your first guess")
    print("good luck!")
    while True:      #game loop
        secret_number = generate_secret_number()
        print(secret_number)  # For testing purposes, you can remove this line in the final version
        chances=10
        start = 0  # Initialize start time
        while chances!=0:
            guess = input("enter your guess: ")
            if start == 0:
                start = time.time()  # Start the timer after the first guess
            if len(guess) != 5 or not guess.isdigit() or len(set(guess)) != 5:
                print("Invalid input. Please enter a 5-digit number with no repeated digits.")
                continue
            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                print(f"It took you {10 - chances + 1} guesses.")
                end = time.time()
                print(f"Time taken: {end - start:.2f} seconds.")
                break
            else:
                for i in range(5):
                    if guess[i] == secret_number[i]:
                        print("+", end=" ")
                    elif guess[i] in secret_number:
                        print("-", end=" ")
                    else:
                        print("*", end=" ")
                chances -= 1
                print(f"   You have {chances} chances left.")
        if chances == 0:
            print(f"Sorry, you have run out of chances. The secret number was {secret_number}.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thank you for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()
