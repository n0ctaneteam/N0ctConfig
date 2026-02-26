from textual.app import ComposeResult
from textual.widgets import Input, Switch
from textual.widget import Widget
from textual.containers import Right

# STRING INPUT
class StringInput(Widget):
    def __init__(self, value: str):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
            yield Input(placeholder="xyz", type="text", compact=True)


# INT INPUT 
class IntegerInput(Widget):
    def __init__(self, value: int):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
            yield Input(placeholder="123", type="integer", compact=True)


# FLOAT INPUT
class FloatInput(Widget):
    def __init__(self, value: float):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
            yield Input(placeholder="123.45", type="number", compact=True)


# BOOL INPUT
class BooleanInput(Widget):
    def __init__(self, value: bool):
        super().__init__()
        self._value = value

    def compose(self) -> ComposeResult:
            yield Switch(value=self._value)