import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# print(logo)

turns_remaining = 0

difficulty_level = input(f"Please choose between easy or hard (1 = easy, 2 = hard): ")
if difficulty_level == "1":
    turns_remaining += 10
elif difficulty_level == "2":
    turns_remaining += 5

player_guessed_number = ""

if difficulty_level == "1":
    print(f"You chose easy")
else:
    print(f"You chose hard")

continue_playing = True
while continue_playing:
    global base_number
    base_number = int(random.randint(1, 100))
    print(base_number)

    while turns_remaining > 0:
        player_guessed_number = int(input(f"Please guess a number between 1-100: "))

        if base_number > player_guessed_number:
            print(f"Guess higher")
        elif base_number < player_guessed_number:
            print(f"Guess lower")
        else:
            print("You guessed it perfectly right!! Wow!")
            continue_playing = False
            break

        turns_remaining -= 1
        print(f"The number of turns remaining is: {turns_remaining}")
    else:
        print("Womp. You ran out of turns. Game Over mannnnn.")

    play_again_option = input(f"Do you want to play again? (Y or N): ").upper()
    if play_again_option != "Y":
        continue_playing = False
