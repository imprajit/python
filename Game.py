import random
print("===== NUMBER GUESSING GAME =====")
difficulty_levels = {
    "easy": 15,
    "medium": 10,
    "hard": 5
}
while True:
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    if difficulty in difficulty_levels:
        break
    print("Invalid difficulty! Please try again.")
max_attempts = difficulty_levels[difficulty]
secret_number = random.randint(1, 100)
attempts = 0
won = False
print("\nGuess a number between 1 and 100!")
print("Maximum attempts:", max_attempts)
while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid integer!")
        continue
    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100!")
        continue
    attempts += 1
    if guess == secret_number:
        print("\nSuperb! You guessed correctly!")
        print("Attempts used:", attempts)
        won = True
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")
    print("Attempts remaining:", max_attempts - attempts)
if not won:
    print("\nTry next time!")
    print("The correct number was:", secret_number)
print("\n===== GAME OVER =====")