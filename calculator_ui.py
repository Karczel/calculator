"""Calculator UI class"""
import tkinter as tk
from tkinter import ttk

from keypad import Keypad
from math import *


class Calculator_UI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.name = "Window"
        self.init_components()

    def init_components(self):
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
        self.add_function = tk.Button(self.frame_f, text='Add', command=self.handle_functions)
        self.history_display = tk.Label(self.frame_f, text=self.output.get(), bg='white', justify="left", anchor='e',
                                font=('Times New Roman', 20, 'normal'))


        # Layout within frame
        self.functions_chooser.pack()
        self.add_function.pack()
        self.history_display.pack()

        # bind
        self.num_keypad.bind(self.handle_digit)
        self.operator_keypad.bind(self.handle_digit)
        self.other_keypad.bind(self.handle_features)

        # Layout
        title.pack(expand=True, fill=tk.BOTH)
        self.display.pack(expand=True, fill=tk.BOTH)
        self.num_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.other_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.frame_f.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def pad(self, keynames, columns, *args):
        return Keypad(self, keynames=keynames, columns=columns)

    def load_functions(self, lst):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(self.frame_f, textvariable=selected)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def handle_features(self, event):
        if event.widget.cget('text') == 'DEL':
            self.output.set(self.output.get()[:-1])
            self.display.config(text=self.output.get())
        elif event.widget.cget('text') == 'CLR':
            self.output.set('')
            self.display.config(text=self.output.get())

    def handle_functions(self):
        self.output.set(self.output.get() + self.function.get())
        self.display.config(text=self.output.get())

    def handle_digit(self, event):
        if event.widget.cget('text') == '=':
            output = self.output.get()
            op = [i.cget('text') for i in self.operator_keypad.buttons]
            op = op[:-2]
            if output[len(output) - 1] not in op \
                    and output[len(output) - 1] not in ['.']:
                self.display.config(fg='black')
                prev = self.output.get()
                try:
                    # fix ^ to **
                    if '^' in self.output.get():
                        self.output.set(self.output.get().replace('^','**'))
                    # fix ln to log
                    if 'ln' in self.output.get():
                        self.output.set(self.output.get().replace('ln', 'log'))
                    self.output.set(eval(self.output.get()))
                    self.display.config(text=self.output.get())
                    self.history.set(self.history.get()
                                     + prev + ' = ' + self.output.get()+'\n')
                    self.history_display.config(text=self.history.get())
                except SyntaxError:
                    self.display.config(fg='red')
            else:
                self.display.config(fg='red')

        else:
            if event.widget.cget('text') != " ":
                new_string = self.output.get() + event.widget.cget('text')
                self.output.set(new_string)
                self.display.config(text=self.output.get())

    def run(self):
        self.mainloop()

    # ---if we were to not use eval()
    #
    # def handle_digit(self, event):
    #     if event.widget.cget('text') == '=':
    #         output = self.output.get()
    #         op = [i.cget('text') for i in self.operator_keypad.buttons]
    #         if output[len(output) - 1] not in op \
    #                 and output[len(output) - 1] not in ['.']:
    #             self.display.config(fg='black')
    #             i = 0
    #             num_list = []
    #             op_list = []
    #             # detect ()
    #             # from ( to ) include in [ ], if there's in side(correct order & number)
    #             open_p = []
    #             close_p = []
    #             # store
    #             while i < len(output):
    #                 # () recursive if found (
    #                 # if ) no leading ( is error
    #                 num_sub = ""
    #                 while output[i] not in op:
    #                     if i >= len(output) - 1:
    #                         break
    #                     num_sub += output[i]
    #                     i += 1
    #                 if i < len(output) - 1:
    #                     num_list.append(num_sub)
    #                     op_list.append(output[i])
    #                 else:
    #                     if num_sub == '':
    #                         num_list.append(output[i])
    #                     else:
    #                         num_list.append(num_sub + output[i])
    #                 i += 1
    #             # turn string to float
    #             # print(num_list)
    #             try:
    #                 num_list = [float(i) for i in num_list]
    #                 # checking
    #                 # print(num_list)
    #                 # print(op_list)
    #                 # order of importance: ^ , / & * , + & - , left to right
    #                 # find highest importance to lowest, then left to right
    #
    #                 self.calculate(num_list, op_list)
    #
    #                 # checking
    #                 # print(num_list)
    #                 # print(op_list)
    #                 self.output.set(str(num_list[0]))
    #                 self.display.config(text=self.output.get())
    #             except ValueError:
    #                 self.display.config(fg='red')
    #         else:
    #             self.display.config(fg='red')
    #
    #     else:
    #         if event.widget.cget('text') != " ":
    #             new_string = self.output.get() + event.widget.cget('text')
    #             self.output.set(new_string)
    #             self.display.config(text=self.output.get())
    #
    # def bracket(self,num_list, op_list):
    # from [[a,c],b] and [[+],-] to [a+c,b] to [a+c-b]
    #
    # def calculate(self, num_list, op_list):
    #     # handle ( )
    #     try:
    #         self.power(num_list, op_list)
    #         self.divide(num_list, op_list)
    #         self.multiply(num_list, op_list)
    #         self.add(num_list, op_list)
    #         self.minus(num_list, op_list)
    #     except IndexError:
    #         pass
    #
    # # seperate helper for each loop, called by order
    # # ^, / & *, + & -
    # def power(self, num_list, op_list):
    #     if len(op_list) == 1:
    #         if op_list[0] == '^':
    #             num_list[0] = num_list[0] ** num_list[1]
    #             num_list.pop(1)
    #             op_list.pop(0)
    #         return None
    #     if op_list[0] == '^':
    #         num_list[0] = num_list[0] ** num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #         return self.power(num_list, op_list)
    #     return self.power(num_list[1:], op_list[1:])
    #
    # def divide(self, num_list, op_list):
    #     if len(op_list) == 1:
    #         if op_list[0] == '/':
    #             num_list[0] = num_list[0] / num_list[1]
    #             num_list.pop(1)
    #             op_list.pop(0)
    #         return None
    #     if op_list[0] == '/':
    #         num_list[0] = num_list[0] / num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #         return self.divide(num_list, op_list)
    #     return self.divide(num_list[1:], op_list[1:])
    #
    # def multiply(self, num_list, op_list):
    #     if len(op_list) == 1:
    #         if op_list[0] == '*':
    #             num_list[0] = num_list[0] * num_list[1]
    #             num_list.pop(1)
    #             op_list.pop(0)
    #         return None
    #     if op_list[0] == '*':
    #         num_list[0] = num_list[0] * num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #         return self.multiply(num_list, op_list)
    #     return self.multiply(num_list[1:], op_list[1:])
    #
    # def add(self, num_list, op_list):
    #     if len(op_list) == 1:
    #         if op_list[0] == '+':
    #             num_list[0] = num_list[0] + num_list[1]
    #             num_list.pop(1)
    #             op_list.pop(0)
    #         return None
    #     if op_list[0] == '+':
    #         num_list[0] = num_list[0] + num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #         return self.add(num_list, op_list)
    #     return self.add(num_list[1:], op_list[1:])
    #
    # def minus(self, num_list, op_list):
    #     if len(op_list) == 1:
    #         if op_list[0] == '-':
    #             num_list[0] = num_list[0] - num_list[1]
    #             num_list.pop(1)
    #             op_list.pop(0)
    #         return None
    #     if op_list[0] == '-':
    #         num_list[0] = num_list[0] - num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #         return self.minus(num_list, op_list)
    #     return self.minus(num_list[1:], op_list[1:])
    #
    # # other functions
    #
