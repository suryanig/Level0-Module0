from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):

        # 4. Ask the user for a guess using a pop-up window, and save their response
        guess = simpledialog.askinteger(title= 'Random Number Guess', prompt= "What is your guess for a number between 1 and 100?")
        # 5. If the guess is correct
        if guess == random_num:
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)
        # 7. if the guess is high
        if guess > random_num:
            # 8. Tell them it's too high
            simpledialog.askstring(title='Your guess is...', prompt = "Your guess if too high. Please try again.")
        # 9. Else if the guess is low
        if guess <= random_num:
            # 10. Tell them it's too low
            simpledialog.askstring(title= 'Your guess is...', prompt = "Your guess is too low. Please try again.")
    #11. Outside of the loop, tell the user they lost
    simpledialog.askstring(title = 'Sorry!', prompt= "Sorry, you ran out of guesses and lost. Try again with a new random number.")
    window.mainloop()
