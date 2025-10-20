import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

COLOR_DIR = Fore.BLUE + Style.BRIGHT
COLOR_FILE = Fore.GREEN

def display_directory_structure(path: Path, prefix: str = '', is_last: bool = False):
    if path.is_dir():
        symbol = '┗ ' if is_last else '┣ '
        print(f"{prefix}{symbol}{COLOR_DIR}📂 {path.name}{Style.RESET_ALL}")
        
        new_prefix = prefix + ('    ' if is_last else '┃   ')
        
        try:
            children = sorted(list(path.iterdir()))
            count = len(children)
            
            for index, child in enumerate(children):
                is_child_last = index == count - 1
                display_directory_structure(child, new_prefix, is_child_last)
        
        except PermissionError:
            print(f"{new_prefix}{Fore.YELLOW}Немає дозволу для доступу до {path.name}{Style.RESET_ALL}")

    elif path.is_file():
        symbol = '┗ 📜 ' if is_last else '┣ 📜 '
        print(f"{prefix}{symbol}{COLOR_FILE}{path.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Необхідно передати шлях до директорії як аргумент.")
        print(f"Використання: python {Path(sys.argv[0]).name} <шлях/до/директорії>")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.")
        sys.exit(1)
    
    if not input_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.")
        sys.exit(1)

    print(f"{COLOR_DIR}📦 {input_path.name}{Style.RESET_ALL}")
    
    children = sorted(list(input_path.iterdir()))
    count = len(children)
    
    for index, child in enumerate(children):
        is_last = index == count - 1
        display_directory_structure(child, prefix=' ', is_last=is_last)


if __name__ == "__main__":
    main()