"""Keypad class"""
import tkinter as tk


class Keypad(tk.Frame):
    """simplifying making keypads in Calculator UI"""

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        """Initialize Keypad Frame"""
        super().__init__()
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        self.frame = super(Keypad, self)
        self.columns = columns
        self.rows = len(self.keynames) // self.columns
        i = 0
        self.buttons = []
        for k in range(self.rows):
            for j in range(self.columns):
                i_key = tk.Button(self, text=self.keynames[i])
                self.buttons.append(i_key)
                i_key.grid(row=k,
                           column=j,
                           sticky=tk.NSEW)
                i += 1
        for i in range(self.rows):
            self.rowconfigure(i, weight=1)
        for i in range(self.columns):
            self.columnconfigure(i, weight=1)

    def bind(self, todo):
        """Bind an event handler to an event sequence."""
        for i in self.buttons:
            i.bind("<Button>", todo)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for i in self.buttons:
            i[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        return self.buttons[0][key]

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for i in self.buttons:
            i.config(**kwargs)

    # Write a property named 'frame' the returns a reference to
    # the superclass object for this keypad.
    # This is so that a programmer can set properties of a keypad's frame,
    # e.g. keypad.frame.configure(background='blue')


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]
    operator = list('*/+-^=')

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    operator = Keypad(root, keynames=operator, columns=1)
    keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    operator.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    root.mainloop()
