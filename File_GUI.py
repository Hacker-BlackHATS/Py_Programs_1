import tkinter as tk

window = tk.Tk()    # A window is an instance of Tkinter’s Tk class.
greeting = tk.Label(text="Hello, Tkinter")      # Use the tk.Label class to add some text to a window
# The window you created earlier doesn’t change.
# You just created a Label widget, but you haven’t added it to the window yet.
# There are several ways to add widgets to a window.
# Right now, you can use the Label widget’s .pack() method
greeting.pack()
"""
Label widgets are used to display text or images. 
The text displayed by a Label widget can’t be edited by the user. 
It’s for display purposes only.
Label widgets display text with the default system text color and the default system text background color. 
These are typically black and white, respectively, but you may see different colors if you have changed these 
settings in your operating system.
"""

label = tk.Label(
    text="Hello, Wizard",
    # foreground="white",  # Set the text color to white
    background="#34A2FE",  # Set the background color to black
    width=20,
    height=20
)
label.pack()
"""
It may seem strange that the label in the window isn’t square even though the width and height 
are both set to 10. This is because the width and height are measured in text units. 
One horizontal text unit is determined by the width of the character "0", or the number zero, in the default system font. 
Similarly, one vertical text unit is determined by the height of the character "0"
"""


window.mainloop()
# window.mainloop() tells Python to run the Tkinter event loop.
# This method listens for events, such as button clicks or keypresses, and
# blocks any code that comes after it from running until the window it’s called on is closed.
