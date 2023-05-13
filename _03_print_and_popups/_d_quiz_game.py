from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window= Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question
    quest1 = simpledialog.askstring(title='Question 1', prompt= "What is 2 + 2?")
    #      // 3.  Use an if statement to check if their answer is correct
    if quest1 == "4":

    #      // 4.  if the user's answer was correct, add one to their score 
        score = score + 1
    else:
        score = score - 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    quest2 = simpledialog.askstring(title='Question 2', prompt= "Are you smart?")
    if quest2 == "yes":
        score = score - 1
    else:
        score = score + 1

    quest3 = simpledialog.askstring(title='Question 3', prompt = "Are there more doors or wheels in the world?")
    if quest3 == "wheels":
        score = score + 1
    else:
        score = score - 1
    # After all the questions have been asked, tell the user their final score

    # remember to convert your variable to a string using the str() function
    simpledialog.askstring(title = 'Final Score', prompt = "Here is your final score:" + str(score))
    # Run the window's .mainloop() method
    window.mainloop()
