import random


words = ["word","dord","mord"]

words_to_guess = words[random.randrange(len(words))]

print(words_to_guess)


hint = ["_"] * len(words_to_guess)
print(hint)

lives = 6

while "_" in hint:
    print(f"")
    guess = input("Guess a leter: ")

    if lives <= 0:
        break
    elif guess .lower() in words_to_guess.lower():
        print("Its in")
        for index in range(len(words_to_guess)):
            if guess.lower() == words_to_guess[index].lower():
                hint[index] = guess
    else:
        lives -= 1
        print(f"lives left: {lives}")

    print(hint)







