# Number-guessing-game-reversed

This is the reverse of the classic number guessing game:  
Instead of you guessing the computer’s number, **the computer guesses the number you’re thinking of** (between 1 and 100).

## How it works
- You think of a number between 1 and 100.
- The computer makes guesses and asks you if the guess is:
  - too high  
  - too low  
  - or correct
- Using a smart strategy (binary search), the computer can usually guess your number in **less than 10 tries**.

## Cheating protection
If you try to cheat (for example, by saying the number is both higher and lower than it should be), the program will detect this and show an error message in the terminal.

## How to run
1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python main.py
   ```
3. Think of a number between 1 and 100.
4. Answer the computer’s questions with:
   - `bigger` for bigger  
   - `smaller` for smaller  
   - `correct` for correct
