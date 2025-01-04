import random

num_guessed = 0
tries = 0

print("Rules: if the computer's guess is bigger than your number then type 'smaller'(no caps) or if the computer's guess is smaller than your number then type 'bigger'(no caps) or the computer's guess was correct then type'correct'(no caps).")
print("I bet I can guess your number in less than 10 tries.")
print("Think of a number between 1 and 100 for the computer to guess")
ready = input("If you are ready to start the game then please type 'start' then press the Enter key! : ").lower()


if ready == "start":
    low = 1
    high = 100
    while True:
        num_guessed = random.randint(low, high)
        print(f"computer's guess is {num_guessed}")
        feedback = input("Is the computer's guess too big or too small or correct? Type 'smaller', 'bigger' or 'correct' : ").lower()

        if feedback == "correct":
            print(f"Yay!, I have guessed your number {num_guessed} in {tries + 1} tries!")
            break
        elif feedback == "smaller":
            high = num_guessed - 1
        elif feedback == "bigger":
            low = num_guessed + 1
        else:
            print("Invalid input!    Please type 'smaller', 'bigger' or 'correct'")

        tries += 1

        if tries > 9:
            print("Ughhhhh! 10 tries for me are over, You beat me this time but you can't beat me next time. Want to play again?")
            break