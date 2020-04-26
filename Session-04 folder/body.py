from pathlib import Path

filename = 'U5.txt'
file_contents = Path(filename).read_text().split('\n')[1:]
print("Body of the U5.txt file: ")
print('\n'.join(file_contents))
