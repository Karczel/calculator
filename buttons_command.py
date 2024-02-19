"""buttons management"""
from abc import ABC, abstractmethod
from math import*


class Command(ABC):
    """Command abstract class"""
    def __init__(self, ui, button):
        """initialize every Command class"""
        self.ui = ui
        self.button = button
        self.value = button.widget.cget('text')

    @abstractmethod
    def handle(self, event):
        """functions to assign to buttons"""


class FeaturesCommand(Command):
    """Handle Features Buttons"""

    def handle(self, event):
        """Handle Features"""
        if event.widget.cget('text') == 'DEL':
            self.ui.output.set(self.ui.output.get()[:-1])
            self.ui.display.config(text=self.ui.output.get())
        elif event.widget.cget('text') == 'CLR':
            self.ui.output.set('')
            self.ui.display.config(text=self.ui.output.get())


class DigitCommand(Command):
    """Handle Digit Buttons"""

    def handle(self, event):
        """Handle Digit"""
        if event.widget.cget('text') != " ":
            new_string = self.ui.output.get() + event.widget.cget('text')
            self.ui.output.set(new_string)
            self.ui.display.config(text=self.ui.output.get())


class OperatorCommand(Command):
    """Handle Operator Buttons"""

    def handle(self, event):
        """Handle Operator"""
        if event.widget.cget('text') == '=':
            output = self.ui.output.get()
            op = [i.cget('text') for i in self.ui.operator_keypad.buttons]
            op = op[:-2]
            if output[len(output) - 1] not in op \
                    and output[len(output) - 1] not in ['.']:
                self.ui.display.config(fg='black')
                self.ui.history.set(self.ui.output.get())
                try:
                    # fix ^ to **
                    if '^' in self.ui.output.get():
                        self.ui.output.set(self.ui.output.get().replace('^', '**'))
                    # fix ln to log
                    if 'ln' in self.ui.output.get():
                        self.ui.output.set(self.ui.output.get().replace('ln', 'log'))
                    self.ui.output.set(eval(self.ui.output.get()))
                    self.ui.display.config(text=self.ui.output.get())
                    # add history buttons
                    self.ui.add_history()
                except SyntaxError:
                    self.ui.display.config(fg='red')
            else:
                self.ui.display.config(fg='red')
        else:
            new_string = self.ui.output.get() + event.widget.cget('text')
            self.ui.output.set(new_string)
            self.ui.display.config(text=self.ui.output.get())


class HistoryCommand(Command):
    """Handle history update"""

    def handle(self, event):
        """Handle History"""
        self.ui.output.set(event.widget.cget('text'))
        self.ui.display.config(text=self.ui.output.get())
