from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical

from .containers import SettingBox

class Section(Vertical):
    def __init__(self, title: str, settings: list[SettingBox]):
        super().__init__()
        self.title = title
        self.settings = settings

    def compose(self) -> ComposeResult:
        self.border_title = self.title
        
        # ANAGH !! here u add the logic for auto rendering settings
        # in a section, just loop through the settings and yield them
        # either use list[SettingBox] or pass whole JSON,
        # in the parameters and then parse it here, whatever is easier for u