lives = 6
secret_word = "jeruk".upper()
secret_word1 = list(secret_word)
count = len(secret_word1)
guess_letter = str(input("Guess letter : ")).upper()
while True:
    if count > 0 and lives > 0:
        validGuess = False:
        while validGuess == False:
            guess = str(input("Guess a letter"))
            countguess = len(guess)
            if countguess > 1:
                validGuess = False
            else: 
                validGuess = True
        
    else:
        print("You Lose")
        break
