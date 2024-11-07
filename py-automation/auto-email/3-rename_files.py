from pathlib import Path

root_dir = Path('auto-email', 'files')

files_path = root_dir.glob('**/*')

for file in files_path:
    print(file)