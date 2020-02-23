from pathlib import Path

filename = 'U5.txt'
file_contents = Path(filename).read_text().split('\n')[1:]
print('\n'.join(file_contents))