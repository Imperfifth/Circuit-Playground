import time
import board
import neopixel
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
userInput = input("Enter a number between 1 and 10, inclusive >> ")
try:
    userInput = int(userInput)
except ValueError:
    print("Not a valid number")
else:
    if userInput >= 0 and userInput <= 10:
        pixels.fill(0, 255, 0)
        count = 0
        while(count < 5):
            guessInput = random.randint(1, 10)
            if(guessInput == userInput):
                pixels.fill(0, 0, 255)
                break
            else:
                pixels.fill(255, 0, 0)
                print("I guessed " + guessInput)
                count += 1
        if count == 5:
            print("I LOSE, I DID NOT GUESS YOUR NUMBER WITHIN 5 TRIES")
        else:
            print("I win!!!!\nI guessed your number in " + str(count) + " tries!!!!!!")
    else:
        print("Not a valid number between 1 and 10")
