"""Calculator UI class"""
import tkinter as tk
from keypad import Keypad


class Calculator_UI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.name = "Window"
        self.init_components()

    def init_components(self):
        self.output = tk.StringVar()

        # Converter
        title = tk.Label(self, text="Converter")

        # Display
        self.display = tk.Label(self, text=self.output.get(), bg='white', justify="left", anchor='e')

        # keypads
        self.num_keypad = self.pad(['7', '8', '9', '4', '5', '6', '1', '2', '3', '00', '0', '.'], 3)
        self.operator_keypad = self.pad(list('*/+-^='), 1)
        self.

        # bind
        self.num_keypad.bind(self.handle_digit)
        self.operator_keypad.bind(self.handle_digit)

        # Layout
        title.pack()
        self.display.pack(expand=True, fill=tk.BOTH)
        self.num_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.operator_keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def pad(self, keynames, columns, *args):
        return Keypad(self, keynames=keynames, columns=columns)

    def handle_digit(self, event):
        if event.widget.cget('text') == '=':
            output = self.output.get()
            op = [i.cget('text') for i in self.operator_keypad.buttons]
            if output[len(output) - 1] not in op \
                    and output[len(output) - 1] not in ['.']:
                # + catch multiple . in one string error
                self.display.config(fg='black')
                i = 0
                num_list = []
                op_list = []
                while i < len(output):
                    num_sub = ""
                    while output[i] not in op:
                        if i >= len(output) - 1:
                            break
                        num_sub += output[i]
                        i += 1
                    if i < len(output) - 1:
                        num_list.append(num_sub)
                        op_list.append(output[i])
                    else:
                        if num_sub == '':
                            num_list.append(output[i])
                        else:
                            num_list.append(num_sub + output[i])
                    i += 1
                # turn string to float
                try:
                    num_list = [float(i) for i in num_list]
                    # checking
                    # print(num_list)
                    # print(op_list)
                    # order of importance: ^ , / & * , + & - , left to right
                    # find highest importance to lowest, then left to right

                    # rough code

                    operator = 0
                    while operator < len(op_list):
                        if op_list[operator] == '^':
                            num_list[operator] = num_list[operator] ** num_list[operator + 1]
                            num_list.pop(operator + 1)
                            op_list.pop(operator)
                        else:
                            operator += 1

                    operator = 0
                    while operator < len(op_list):
                        if op_list[operator] == '*':
                            num_list[operator] = num_list[operator] * num_list[operator + 1]
                            num_list.pop(operator + 1)
                            op_list.pop(operator)
                        elif op_list[operator] == '/':
                            num_list[operator] = num_list[operator] / num_list[operator + 1]
                            num_list.pop(operator + 1)
                            op_list.pop(operator)
                        else:
                            operator += 1

                    operator = 0
                    while operator < len(op_list):
                        if op_list[operator] == '+':
                            num_list[operator] = num_list[operator] + num_list[operator + 1]
                            num_list.pop(operator + 1)
                            op_list.pop(operator)
                        elif op_list[operator] == '-':
                            num_list[operator] = num_list[operator] - num_list[operator + 1]
                            num_list.pop(operator + 1)
                            op_list.pop(operator)
                        else:
                            operator += 1

                    # print(num_list)
                    # print(op_list)
                    self.output.set(str(num_list[0]))
                    self.display.config(text=self.output.get())
                except ValueError:
                    self.display.config(fg='red')
            else:
                self.display.config(fg='red')

        else:
            if event.widget.cget('text') != " ":
                new_string = self.output.get() + event.widget.cget('text')
                self.output.set(new_string)
                self.display.config(text=self.output.get())

    # def calculate(self,num_list, op_list):
    # if len(op_list) == 1:
    #     if op_list[0] == '^':
    #         num_list[0] = num_list[0] ** num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #     elif op_list[0] == '/':
    #         num_list[0] = num_list[0] / num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #     elif op_list[0] == '*':
    #         num_list[0] = num_list[0] * num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #     elif op_list[0] == '+':
    #         num_list[0] = num_list[0] + num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    #     elif op_list[0] == '-':
    #         num_list[0] = num_list[0] - num_list[1]
    #         num_list.pop(1)
    #         op_list.pop(0)
    # if op_list[0] == '^':
    #     num_list[0] = num_list[0] ** num_list[1]
    #     num_list.pop(1)
    #     op_list.pop(0)
    #     return self.calculate()
    # elif op_list[0] ==
    # return num_list,op_list

    # seperate helper for each loop, called by order
    # # ^, / & *, + & -
    # def ^
    #
    # def /
    #
    # def *
    #
    # def +
    #
    # def -

    def run(self):
        self.mainloop()
