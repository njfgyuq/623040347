i = 2
ans_word = "Heart"

while True:
    word = input("Enter a word: ")
    if i == 0:
        print("Incorrect! You have 0 guesses left.")
        print("Thanks for trying, but the secret word is "
            "actually: %s" % ans_word)
        break
    elif word == ans_word:
        print("Congrats that you can guess the secret word correctly")
        break
    elif word != ans_word:
        print(f"Incorrect! You have {i} guesses left.")
        i -= 1
