from pathlib import Path
import os
import shutil

TEMPLATE_DIR = Path(os.path.dirname(__file__)).joinpath('template')
TEMPLATE_NAME_LIST = [
    '.flake8',
    'ruff.toml',
    '.vscode',
    '.vscode/settings.json',
    '.vscode/extensions.json',
]
CWD = Path.cwd()


def create_template(cwd: Path, template_dir: Path, template_name: str) -> bool:
    target = cwd.joinpath(template_name)
    if not target.exists():
        print(f'Create {template_name}')
        if target.is_dir():
            target.mkdir()
            return True
        elif target.is_file():
            shutil.copy(target, template_dir.joinpath(template_name))
            return True
    print(f'{template_name} already exists')
    return False


def main():
    for template_name in TEMPLATE_NAME_LIST:
        create_template(CWD, TEMPLATE_DIR, template_name)


if __name__ == '__main__':
    main()
