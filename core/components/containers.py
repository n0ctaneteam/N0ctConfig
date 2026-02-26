from textual.app import ComposeResult
from textual.widgets import Label, Static
from textual.containers import Horizontal,Vertical,Right

from .inputs import StringInput, IntegerInput, FloatInput, BooleanInput

class SettingBox(Horizontal):
    # this takes a NAME, KEY, TYPE, VALUE, DESCRIPTION and renders it in a nice way in the tui
    def __init__(self, name: str, key: str, type: str, value: str, description: str):
        super().__init__()
        self._name = name
        self._key = key
        self._type = type
        self._value = value
        self._description = description

    def compose(self) -> ComposeResult:
        self.border_title = self._name
        with Vertical(classes="setting-info"):
            # yield Label(f"{self._name} ({self._type})")
            yield Static(f"Desc: {self._description}", classes="setting-desc")
        with Horizontal(classes="setting-input"):
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