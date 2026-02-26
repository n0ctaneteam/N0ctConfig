from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Horizontal,Vertical

from .inputs import StringInput, IntegerInput, FloatInput, BooleanInput

class SettingBox(Vertical):
    # this takes a NAME, KEY, TYPE, VALUE, DESCRIPTION and renders it in a nice way in the tui
    def __init__(self, name: str, key: str, type: str, value: str, description: str):
        super().__init__()
        self._name = name
        self._key = key
        self._type = type
        self._value = value
        self._description = description

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label(f"{self._name} ({self._type})")
            match self._type:
                # for now we only support string inputs, but we can easily add more types in the future
                case "string":
                    yield StringInput(self._value);
                case "integer":
                    yield IntegerInput(self._value);
                case "float":
                    yield FloatInput(self._value);
                case "bool":
                    yield BooleanInput(self._value);
        yield Label(f"Desc: {self._description}")