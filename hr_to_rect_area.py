import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area Calculator")
    frm_main.pack(padx=41, pady=31, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Width:"
    lbl_width = Label(frm_main, text="Width:")

    # Create a label that displays "Height"
    lbl_height = Label(frm_main, text="Height:")

    # Create a label that displays a warning to not use negative integers
    lbl_warning = Label(frm_main, text="Do NOT use Negative Integers (-1, -2, etc)")

    # Create an integer entry box where the user will enter her age.
    ent_width = IntEntry(frm_main, width=4, lower_bound=0,)

    # Create an integer entry box where the user will enter her age.
    ent_height = IntEntry(frm_main, width=4, lower_bound=0,)

    # Create a label that displays "units"
    lbl_width_units = Label(frm_main, text="units")
    lbl_height_units = Label(frm_main, text="units")


    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_calculated_area = Label(frm_main, width=3)
    lbl_calculated_area_units = Label(frm_main, text="units")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(row=0, column=0, padx=3, pady=3)
    ent_width.grid(row=0, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=0, column=2, padx=0, pady=3)
    #
    lbl_height.grid(row=1, column=0, padx=3, pady=3)
    ent_height.grid(row=1, column=1, padx=3, pady=3)
    lbl_height_units.grid(row=1, column=2, padx=0, pady=3)
    #
    #
    lbl_area.grid(row=2, column=0, padx=3, pady=3)
    lbl_calculated_area.grid(row=2, column=1, padx=3, pady=3)    
    lbl_calculated_area_units.grid(row=2, column=2, padx=0, pady=3)
    #
    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's intended width.
            width = ent_width.get()

            # Get the user's intended height.
            height = ent_height.get()

            # Compute the user's area from the user's width and height.
            area = width * height

            # Display the calculated area
            lbl_calculated_area.config(text=f"{area:.0f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_calculated_area.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_height.clear()
        lbl_calculated_area.config(text="")
        ent_width.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_width.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_width.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
