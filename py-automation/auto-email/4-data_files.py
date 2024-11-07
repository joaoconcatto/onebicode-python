from pathlib import Path
from datetime import datetime


path_teste2 = Path('auto-email', 'files', 'dados2', 'teste2.txt')

# informacoes de data e hora do arquivo
stats = path_teste2.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)