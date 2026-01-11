lives = 6
secret_word = "jeruk".upper()
secret_word1 = list(secret_word)
count = len(secret_word1)
display_word = count * ["_"]
while True:
    if "_" in display_word and lives > 0:
        validGuess = False
        print("".join(display_word))

        while validGuess == False:
            guess = input("Guess a letter : ").upper()
            countguess = len(guess)
            if countguess > 1:
                print("Please guess one letter at a time.")
                validGuess = False
            else: 
                validGuess = True
    
        if guess in secret_word1:
            print(guess, "is part of the word.")
            for num in range(len(secret_word1)):
                if secret_word1[num] == guess:
                    display_word[num] = guess
        else:
            print(guess, "is not part of the word.")
            lives = lives - 1
    elif lives <= 0:
        print("You Lose")
        break
    else:
        print("You Win!")
        break
