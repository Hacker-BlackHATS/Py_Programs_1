import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

"""
There are three essential elements in the application :
  1. A Button widget called btn_open for opening a file for editing
  2. A Button widget called btn_save for saving a file
  3. A TextBox widget called txt_edit for creating and editing the text file

The three widgets will be arranged so that the two buttons are on the left-hand 
side of the window, and the text box is on the right-hand side. 
The whole window should have a minimum height of 800 pixels, 
and txt_edit should have a minimum width of 800 pixels. 
The whole layout should be responsive so that if the window is resized, 
then txt_edit is resized as well. The width of the Frame holding the buttons should not change, however.
"""


def open_file():
    """Open a file for editing."""
    # Use the askopenfilename dialog from the tkinter.
    # filedialog module to display a file open dialog and store the selected file path to filepath.
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # Check to see if the user closes the dialog box or clicks the Cancel button.
    # If so, then filepath will be None, and the function will return without executing
    # any of the code to read the file and set the text of txt_edit
    if not filepath:
        return

    txt_edit.delete(1.0, tk.END)    # Clears the current contents of txt_edit using .delete().
    # Open the selected file
    with open(filepath, "r") as input_file:
        text = input_file.read()    # .read() its contents before storing the text as a string.
        txt_edit.insert(tk.END, text)   # Assigns the string text to txt_edit using .insert().
    # Sets the title of the window so that it contains the path of the open file.
    window.title(f"Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    # Use the asksaveasfilename dialog box to get the desired save location from the user.
    # The selected file path is stored in the filepath variable.
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    # Check to see if the user closes the dialog box or clicks the Cancel button.
    # If so, then filepath will be None, and the function will return without
    # executing any of the code to save the text to a file.
    if not filepath:
        return
    # Creates a new file at the selected file path.
    with open(filepath, "w") as output_file:
        # Extracts the text from txt_edit with .get() method and assigns it to the variable text.
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)     # Writes text to the output file.
    # Updates the title of the window so that the new file path is displayed in the window title.
    window.title(f"Text Editor - {filepath}")


window = tk.Tk()
window.title("Text Editor(BASIC)")

"""
To set the minimum sizes for the window and txt_edit, you can set the minsize parameters of the 
window methods .rowconfigure() and .columnconfigure() to 800. 
To handle resizing, you can set the weight parameters of these methods to 1.
"""

# set the row and column configurations.
window.rowconfigure(0, minsize=800, weight=1)

"""
The first argument is 0, which sets the height of the first row to 800 pixels 
and makes sure that the height of the row grows proportionally to the height 
of the window. There’s only one row in the application layout, so these settings apply to the entire window.
"""

window.columnconfigure(1, minsize=800, weight=1)

"""
Here, you use .columnconfigure() to set the width and weight attributes of the column with index 1 to 800 and 1,

Remember, row and column indices are zero-based, so these settings apply only to 
the second column. By configuring just the second column, the text box will expand 
and contract naturally when the window is resized, while the column containing the buttons will remain at a fixed width.
"""

# create the four widgets you’ll need for the text box, the frame, and the open and save buttons.
# In order to get both buttons into the same column, you’ll need to create a Frame widget called fr_buttons.

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

"""
The above two lines of code create a grid with two rows and one column in the fr_buttons 
frame since both btn_open and btn_save have their master attribute set to fr_buttons. 
btn_open is put in the first row and btn_save in the second row so that btn_open appears above btn_save in the layout

Both btn_open and btn_save have their sticky attributes set to "ew", which forces the buttons to expand horizontally 
in both directions and fill the entire frame. This makes sure both buttons are the same size.

You place 5 pixels of padding around each button by setting the padx and pady parameters to 5. 
Only btn_open has vertical padding. Since it’s on top, the vertical padding offsets the button down from the top 
of the window a bit and makes sure that there’s a small gap between it and btn_save.
"""

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

"""
These two lines of code create a grid with one row and two columns for window. 
You place fr_buttons in the first column and txt_edit in the second column so that 
fr_buttons appears to the left of txt_edit in the window layout.

The sticky parameter for fr_buttons is set to "ns", which forces the whole frame to expand 
vertically and fill the entire height of its column. txt_edit fills its entire grid cell 
because you set its sticky parameter to "nsew", which forces it to expand in every direction.
"""

window.mainloop()
