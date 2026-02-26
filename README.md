# N0ct-Ecosystem Configurator TUI app
### This app provides TUI to manage and configure N0ct-xyz apps/softwares/bundles... made under project [N0ctOS](https://n0ctaneteam.github.io/N0ctOS)

### <b><u>Those are</u></b>
- [N0ctBar](https://github.com/n0ctaneteam/N0ctBar) ==> waybar + quickshell + swaync 
- N0ctHypr ==> hypr dotfiles, but tweaked for config compatibility

## Architecture
```
N0ctConfig
├── 📂core
│   ├── 📂components (buttuns,panels etc)
│   │   ├── ▶️panels.py
│   │   ├── ▶️buttons.py
│   │   ├── ▶️inputs.py
│   │   └── ...
│   └── 📂scripts (updater,downloader etc)
│       ├── ▶️update.py
│       ├── ▶️moduleDownloader.py
│       └── ...
├── 📂modules
│   ├── module1
│   │   ├── 📂some-folder
│   │   ├── 📂some-more-folders
│   │   ├── ▶️main.py (main content)
│   │   └── ▶️quick.py (optional, quicksettings)
│   ├── module2
│   │   ├── ... 
│   │   └── ▶️main.py (main tabbed content)
│   └── ...
├── ▶️main.py
├── ▶️loader.py
└── 🧰cachecleaner.sh
```
🧰cachecleaner.sh is a dev util, that u may run in BG to clear up annoying __pycache__ folders during runtime