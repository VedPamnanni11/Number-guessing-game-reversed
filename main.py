import random

play_again = "yes"

print("Rules: if the computer's guess is bigger than your number then type 'smaller' or if the computer's guess is smaller than your number then type 'bigger' or the computer's guess was correct then type'correct'.")
print("I bet I can guess your number in less than 10 tries.")
print("Think of a number between 1 and 100 for the computer to guess")

while play_again == 'yes':

    num_guessed = 0
    tries = 0

    play_again = input("If you are ready to start the game then please type 'yes' then press the Enter key! : ").lower()


    if play_again == "yes":
        low = 1
        high = 100
        while True:
            num_guessed = random.randint(low, high)
            print(f"computer's guess is {num_guessed}")
            feedback = input("Is the computer's guess too big or too small or correct? Type 'smaller', 'bigger' or 'correct' : ").lower()

            if feedback == "correct":
                play_again = input(f"Yay!, I have guessed your number {num_guessed} in {tries + 1} tries!, Do you want to play again? : ").lower()
                break
            elif feedback == "smaller":
                high = num_guessed - 1
            elif feedback == "bigger":
                low = num_guessed + 1
            else:
                print("Invalid input! Please type 'smaller', 'bigger' or 'correct'.")
                continue

            tries += 1

            if tries == 10:
                play_again = input("Ughhhhh! 10 tries for me are over, You beat me this time but you can't beat me next time. Want to play again?, Then type 'yes' or 'no' if you want to stop the program : ").lower()
                break