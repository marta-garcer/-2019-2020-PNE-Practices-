from pathlib import Path
filename = 'RNU6_269P.txt'
file_contents = Path(filename).read_text().split('\n')[0]
print('First line of the RNU6_269P.txt file:'  )
print(file_contents)