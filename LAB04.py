import random

wordlist = ["apel", "mangga", "pisang", "jeruk"]

wins = 0
losses = 0

def round():
    global wins, losses
    lives = 5

    secret_word2 = random.choice(wordlist)
    secret_word = secret_word2.upper()
    secret_word1 = list(secret_word)
    count = len(secret_word1)
    display_word = count * ["_"]
    used_words = set()
    while True:
        if "_" in display_word and lives >= 0:
            validGuess = False
            print("+--------------------------+")
            print(" ")
            print("Chances :", lives + 1)
            print("".join(display_word))

            while validGuess == False:
                guess = input("Guess a letter : ").upper()
                print(" ")
                countguess = len(guess)
                if countguess > 1 or not guess.isalpha():
                    print("Invalid input. Try Again")
                    print(" ")
                    print("+--------------------------+")
                    validGuess = False
                else: 
                    if guess in used_words:
                        print("You have already guessed that letter.")
                        print("+--------------------------+")
                        validGuess = False
                    else:
                        used_words.add(guess)
                        validGuess = True

        
            if guess in secret_word1:
                print(guess, "is part of the word.")
                for num in range(count):
                    if secret_word1[num] == guess:
                        display_word[num] = guess
            else:
                print(guess, "is not part of the word.")

            lives -= 1
        
            if "_" not in display_word:
                print("+--------------------------+")
                print(" ")
                print("You Win!")
                print("The word was,", secret_word)
                print(" ")
                print("+--------------------------+")
                wins += 1
                break

            if lives < 0:
                print("+--------------------------+")
                print(" ")
                print("You Lose")
                print("The word was,", secret_word)
                print(" ")
                print("+--------------------------+")
                losses += 1
                break
            
    wordlist.remove(secret_word2)
            

while True:
    round()

    if not wordlist:
        print(" ")
        print("No more words left")
        break
    print(" ")
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again == "n":
        break
    if play_again == "y":
        continue
    else:
        print(" ")
        print("+--------------------------+")
        print(" ")
        print("Invalid input, exiting game")
        break

print(" ")
print("+--------------------------+")
print(" ")
print("Total Wins :", wins, ", Total Losses :", losses)
print(" ")
print("+--------------------------+")

