from pathlib import Path
import os
import shutil

TEMPLATE_DIR = Path(os.path.dirname(__file__)).joinpath('template')
print(TEMPLATE_DIR)

CWD = Path(os.getcwd())


def main():
    if not CWD.joinpath('.flake8').is_file():
        print('Create .flake8')
        shutil.copy(TEMPLATE_DIR.joinpath('.flake8'), CWD.joinpath('.flake8'))
    else:
        print('.flake8 already exists')

    if not CWD.joinpath('ruff.toml').is_file():
        print('Create ruff.toml')
        shutil.copy(TEMPLATE_DIR.joinpath('ruff.toml'), CWD.joinpath('ruff.toml'))
    else:
        print('ruff.toml already exists')

    if not CWD.joinpath('.vscode').is_dir():
        print('Create .vscode')
        CWD.joinpath('.vscode').mkdir()
    else:
        print('.vscode already exists')

    if not CWD.joinpath('.vscode/settings.json').is_file():
        print('Create .vscode/settings.json')
        shutil.copy(
            TEMPLATE_DIR.joinpath('.vscode/settings.json'),
            CWD.joinpath('.vscode/settings.json'),
        )
    else:
        print('.vscode/settings.json exists already')

    if not CWD.joinpath('.vscode/extensions.json').is_file():
        print('Create .vscode/extensions.json')
        shutil.copy(
            TEMPLATE_DIR.joinpath('.vscode/extensions.json'),
            CWD.joinpath('.vscode/extensions.json'),
        )
    else:
        print('.vscode/extensions.json exists already')
