__author__ = 'pooja'

#First time the game is played
gameOn = True
#Input name & display welcome message
name = input("Hi! What is your name? ")
print("Hello " + name + "! Let's play a game!\nThink of random number from 1 to 100, and I'll try to guess it!")

#While the user is still playing the game
while(gameOn):
    #The number is not yet guessed
    guessed = False
    #Count of guesses
    guess = 0
    #Initialize the range of the game: 0 to 100
    low = 0
    high = 100

    while(not guessed):
        guess = guess + 1
        replyToGuess = input("Is it " + str((low + high)//2) + " (yes/no):")
        if(replyToGuess.lower() == "no"):
            replyToRange = input("Is the number larger than " + str((low + high)//2) + " (yes/no):")
            if(replyToRange == "no"):
                high = (low + high)//2;
            else:
                low = (low + high)//2;
        else:
            guessed = True
            print("Yeey! I got it in "+ str(guess) + " tries!")

    playMore = input("Do you want to play more? (yes/no):")
    if(playMore.lower() == "yes"):
        continue
    else:
        break

print("Bye-Bye")






