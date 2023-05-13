from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    var = random.randint(0,3)
    # 2. Print your variable to the console
    print(var)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring(title = 'Awesome', prompt="What is something that you think is awesome")
    # 4. If your variable is  0
    if var == 0:
        # -- tell the user whatever they entered is awesome!
        simpledialog.askstring(title = 'Awesome!', prompt = "Woah! That's awesome")
    # 5. If your variable is  1
    if var == 1:
        # -- tell the user whatever they entered is ok.
        simpledialog.askstring(title = 'Ok', prompt = "That's ok I guess.")
    # 6. If your variable is  2
    if var == 2:
        # -- tell the user whatever they entered is boring.
        simpledialog.askstring(title = 'Boring', prompt= "That's so boring. How dare you!")
    # 7. If your variable is  3
    if var == 3:
        # -- invent your own message to give to the user (be nice).
        simpledialog.askstring(title = 'Interesting...', prompt = "That's interesting. I've never tried it.")
    # Run the window's .mainloop() method
    window.mainloop()
