from pathlib import Path
filename = 'ADA.txt'
file_contents = Path(filename).read_text().split('\n')[1:]
new_file ="".join(file_contents)
print(len(new_file))