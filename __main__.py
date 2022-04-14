"""The main app that runs all the code."""

import tkinter

class Window(tkinter.Tk):
    """The main window."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__ == "__main__":
    root = Window()
    root.mainloop()