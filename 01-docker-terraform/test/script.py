from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name # wraps it in Path object, giving you access to all of pathlib

print(f"Files in {current_dir}:")
print(f'{__file__}')
print()
print(Path(__file__).read_text()) # outputs the entire script
print(current_file) # outputs script.py
print('\n\n')

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encoding='utf-8')
        print(f"    Content: {content}")