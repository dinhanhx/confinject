import os
import shutil
from pathlib import Path

cwd = Path(os.getcwd())
print(cwd)

with open('configs/.flake8', 'r', encoding='utf-8') as flake8:
    if not cwd.joinpath('.flake8').is_file():
        print('Create .flake8')
        with open(cwd.joinpath('.flake8'), 'w', encoding='utf-8') as new_flake8:
            new_flake8.write(flake8.read())
    else:
        print('.flake8 exists already')

with open('configs/ruff.toml', 'r', encoding='utf-8') as ruff:
    if not cwd.joinpath('ruff.toml').is_file():
        print('Create ruff.toml')
        with open(cwd.joinpath('ruff.toml'), 'w', encoding='utf-8') as new_ruff:
            new_ruff.write(ruff.read())
    else:
        print('.ruff.toml exists already')

if not cwd.joinpath('.vscode').is_dir():
    print('Create .vscode')
    cwd.joinpath('.vscode').mkdir()
else:
    print('.vscode exists already')

if not cwd.joinpath('.vscode/settings.json').is_file():
    print('Create .vscode/settings.json')
    shutil.copy('configs/.vscode/settings.json', cwd.joinpath('.vscode/settings.json'))
else:
    print('.vscode/settings.json exists already')

if not cwd.joinpath('.vscode/extensions.json').is_file():
    print('Create .vscode/extensions.json')
    shutil.copy('configs/.vscode/extensions.json', cwd.joinpath('.vscode/extensions.json'))
else:
    print('.vscode/extensions.json exists already')
