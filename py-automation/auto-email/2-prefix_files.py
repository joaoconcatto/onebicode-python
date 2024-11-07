from pathlib import Path

root_dir = Path('auto-email', 'files')
files_path = root_dir.iterdir()

for file in files_path:
    new_filename = f'new-{file.stem}{file.suffix}'
    new_filepath = file.with_name(new_filename)
    file.rename(new_filepath)