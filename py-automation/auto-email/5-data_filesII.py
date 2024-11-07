from pathlib import Path
from datetime import datetime

root_dir = Path('auto-email', 'files')

for file in root_dir.glob('**/*'):
    if file.is_file():
        stats = file.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%Y-%m-%d')
        
        new_filename = f'{date_created_str} - {file.name}'
        print(new_filename)

        new_filepath = file.with_name(new_filename)
        file.rename(new_filepath)