def main():
    try:
        userInput = input("ENTER A NUMBER BETWEEN 0 AND 9 INCLUDED")
        userInput = int(userInput)
    except ValueError:
        print("Pleaes enter an integer")
    else:
        count = 0
        for i in range(0, 11):
            if(userInput == i):
                print("The User variable is equal to the count variable. User = " + str(userInput) + " Count variable = " + str(i))
main()
