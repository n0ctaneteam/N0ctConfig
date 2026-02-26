# core/main.py

from textual.app import App, ComposeResult
from textual.widgets import ContentSwitcher, Tabs , Footer, TabbedContent, TabPane, Static, Input

from loader import discover_modules

from core.components.panels import Section
from core.components.containers import SettingBox

class CoreApp(App):
    # css files
    CSS_PATH = "./core/components/containers.tcss"
    
    # keybinds
    BINDINGS = [     
    ("q", "quit", "Quit") 
    ]

    modules, tabs = discover_modules()
    def compose(self) -> ComposeResult:
        yield SettingBox("Test Setting", "test_setting", "string", "Hello World", "This is a test setting description")
        yield SettingBox("Test Setting 2", "test_setting_2", "bool", False, "This is another test setting description")
        yield SettingBox("Test Setting 3", "test_setting_3", "integer", 10, "This is yet another test setting description")
        yield SettingBox("Test Setting 4", "test_setting_4", "float", 3.14, "This is yet another test setting description")
        with TabbedContent():
            for module, tab in zip(self.modules, self.tabs):
                with TabPane(tab):
                    yield module.Render()
        
        yield Input(placeholder="Type something...")
        
        yield Footer()

if __name__ == "__main__":
    CoreApp().run()
