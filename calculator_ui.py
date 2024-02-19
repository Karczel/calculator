"""Calculator UI class"""
import tkinter as tk
from tkinter import ttk

from math import *

from History import History
from keypad import Keypad
from buttons_command import *


class Calculator_UI(tk.Tk):
    """My Calculaotr UI"""

    def __init__(self):
        """Initialize Calculator User Interface"""
        super().__init__()
        self.name = "Window"
        self.init_components()

    def init_components(self):
        """init_components"""
        self.output = tk.StringVar()
        self.history = tk.StringVar()

        # Converter
        title = tk.Label(self, text="Converter", bg='black', fg='white', font=('Times New Roman', 50, 'normal'))

        # Display
        self.display = tk.Label(self, text=self.output.get(), bg='white', justify="left", anchor='e',
                                font=('Times New Roman', 50, 'normal'))

        # keypads
        self.num_keypad = self.pad(list('789456123 0.'), 3)
        self.operator_keypad = self.pad(list('*/+-^=%()'), 1)
        self.other_keypad = self.pad(['DEL', 'CLR'], 1)

        # functions
        self.frame_f = tk.Frame(self)
        self.function, self.functions_chooser = self.load_functions(['exp', 'ln', 'log10', 'log2', 'sqrt'])
        self.add_function = tk.Button(self.frame_f, text='Add', command=self.handle_functions,
                                      font=('Times New Roman', 25, 'normal'), fg="blue")

        # Layout within frame
        self.functions_chooser.pack()
        self.add_function.pack()

        # bind
        self.num_keypad.bind(self.handle_digit)
        self.operator_keypad.bind(self.handle_operator)
        self.other_keypad.bind(self.handle_features)

        # config aesthetics
        self.num_keypad.configure(font=('Times New Roman', 25, 'normal'), fg="blue")
        self.operator_keypad.configure(font=('Times New Roman', 25, 'normal'), fg="blue")
        self.other_keypad.configure(font=('Times New Roman', 25, 'normal'), fg="blue")

        # Layout
        title.pack(expand=True, fill=tk.BOTH)
        self.display.pack(expand=True, fill=tk.BOTH)
        self.num_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.other_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_f.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def pad(self, keynames, columns, *args):
        """simplifying KeypaDs initializing method"""
        return Keypad(self, keynames=keynames, columns=columns)

    def load_functions(self, lst):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(self.frame_f, textvariable=selected, font=('Times New Roman', 25, 'normal'))
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def handle_features(self, event):
        """"handle DEL, CLR buttons"""
        FeaturesCommand(self, event).handle(event)

    def handle_functions(self):
        """handle functions in combobox"""
        # not in Command class due to being combobox, and thus has not button attribute
        self.output.set(self.output.get() + self.function.get())
        self.display.config(text=self.output.get())

    def handle_digit(self, event):
        """handle numbers keypad and operators keypad"""
        DigitCommand(self, event).handle(event)

    def handle_operator(self, event):
        """handle numbers keypad and operators keypad"""
        OperatorCommand(self, event).handle(event)

    def handle_history(self, event):
        """handle history buttons"""
        HistoryCommand(self, event).handle(event)

    def add_history(self, *args):
        """add buttons as history features"""
        History(self).add_history()

    def run(self):
        """run UI"""
        self.mainloop()
