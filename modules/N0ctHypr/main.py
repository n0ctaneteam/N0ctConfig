from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical

class Render(Vertical):
    def compose(self) -> ComposeResult:
        yield Label("Hyprland Module")