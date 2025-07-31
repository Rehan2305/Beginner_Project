import random

print("Hey there! Let's play a quick guessing game.")
print("I'm thinking of a number between 1 and 10.")

number = random.randint(1, 10)
guess = int(input("Take a guess: "))

if guess == number:
    print("Wow! You got it right 🎉")
else:
    print(f"Oops! I was thinking of {number}. Better luck next time 😉")
