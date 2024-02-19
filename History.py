"""History class to update history section, invoked everytime calculation is successful"""
import tkinter as tk


class History:
    def __init__(self, ui):
        """Initialize History object"""
        self.ui = ui

    def add_history(self, *args):
        """add buttons as history features"""
        button_frame = tk.Frame(self.ui.frame_f)
        new_history = tk.Button(button_frame, text=self.ui.history.get(), font=('Times New '
                                                                                'Roman', 20,
                                                                                'normal'))
        new_output_his = tk.Button(button_frame, text=self.ui.output.get(), font=('Times New '
                                                                                  'Roman',
                                                                                  20,
                                                                                  'normal'))
        new_history.bind('<Button>', self.ui.handle_history)
        new_output_his.bind('<Button>', self.ui.handle_history)
        equal_sign = tk.Label(button_frame, text='=', font=('Times New Roman', 20, 'normal'))
        new_history.pack(side=tk.LEFT, expand=True, fill=tk.X, anchor=tk.N)
        new_output_his.pack(side=tk.RIGHT, expand=True, fill=tk.X, anchor=tk.N)
        equal_sign.pack(side=tk.RIGHT, expand=True, fill=tk.X, anchor=tk.N)
        button_frame.pack(expand=True, fill=tk.X, anchor=tk.N)
