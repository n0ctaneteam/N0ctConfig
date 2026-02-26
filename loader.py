import importlib
from pathlib import Path

def discover_modules():
    base_path = Path("modules")
    folders = [p.name for p in base_path.iterdir() if p.is_dir()]
    
    tabs = []
    modules = []
    for folder in folders:
        if folder.startswith("__"):
            break
        mod = importlib.import_module(f"modules.{folder}.main")
        modules.append(mod)
        
        tabs.append(folder)

    return modules, tabs
