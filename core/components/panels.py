from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import VerticalScroll

class Section(VerticalScroll):
    def __init__(self, title: str, settings: list[dict]):
        super().__init__()
        self.title = title
        self.settings = settings

    def compose(self) -> ComposeResult:
        yield Label(f"======== {self.title} ========")
        for setting in self.settings:
            yield Label(f"{setting['name']}: {setting['value']}")