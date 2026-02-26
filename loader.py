import importlib
from pathlib import Path

def discover_modules():
    BASE_DIR = Path(__file__).resolve().parent
    MODULES_DIR = BASE_DIR / "modules"
    folders = [p.name for p in MODULES_DIR.iterdir() if p.is_dir()]
    
    tabs = []
    modules = []
    for folder in folders:
        if folder.startswith("__"):
            break
        mod = importlib.import_module(f"modules.{folder}.main")
        modules.append(mod)
        
        tabs.append(folder)

    return modules, tabs
