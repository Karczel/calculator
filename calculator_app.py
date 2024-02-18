"""Display the calculator user interface."""
from calculator_ui import Calculator_UI


if __name__ == '__main__':
    # create the UI.  There is no controller (yet), so nothing to inject.
    ui = Calculator_UI()
    ui.run()
