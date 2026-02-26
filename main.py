# core/main.py

from textual.app import App, ComposeResult
from textual.widgets import ContentSwitcher, Tabs , Footer, TabbedContent, TabPane, Static

from loader import discover_modules


class CoreApp(App):
    BINDINGS = [     
    ("q", "quit", "Quit") 
    ]

    modules, tabs = discover_modules()
    def compose(self) -> ComposeResult:
        with TabbedContent():
            for module, tab in zip(self.modules, self.tabs):
                with TabPane(tab):
                    yield module.Render()
                
        yield Footer()

if __name__ == "__main__":
    CoreApp().run()
