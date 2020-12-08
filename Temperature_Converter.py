import tkinter as tk
"""
You need three elements :
  1. An Entry widget called ent_temperature to enter the Fahrenheit value
  2. A Label widget called lbl_result to display the Celsius result
  3. A Button widget called btn_convert that reads the value from the Entry widget,
     converts it from Fahrenheit to Celsius, and sets the text of the Label widget to
     the result when clicked.

"""


def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
"""
ent_temperature is where the user will enter the Fahrenheit value. 
lbl_temp is used to label ent_temperature with the Fahrenheit symbol. 
frm_entry is a container that groups ent_temperature and lbl_temp together.

You want lbl_temp to be placed directly to the right of ent_temperature. 
You can lay them out in the frm_entry using the .grid() geometry manager with one row and two columns.
You’ve set the sticky parameter to "e" for ent_temperature so that it always sticks to the right-most 
edge of its grid cell. You also set sticky to "w" for lbl_temp to keep it stuck to the left-most edge 
of its grid cell. This ensures that lbl_temp is always located immediately to the right of ent_temperature.
"""
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()


# e1 = tk.Entry()
# e1.pack()
# l1 = tk.Label(text="F")
# l1.pack()
# b1 = tk.Button(master=conversion_F_to_C(e1), text="Convert")

window.mainloop()
