hidden_word = "Coffee"
tries = 0
print('Guess the word!')
print('The word is 6 letters long. ')

guess = input("Guess the word: ")
while guess != "0" :
    if guess == hidden_word:
        print("You guessed the word!")

    else:
        print("Wrong guess. Try again. ")
        tries += 1
        if tries == 3:
            print("Hint: Something you drink in the mornings!")

    guess = input("Guess the word (or 0 to quit): ")

print("Thank you for playing!")


