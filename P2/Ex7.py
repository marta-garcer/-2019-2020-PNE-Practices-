from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "10.3.33.54"
PORT = 8086
PORT2 = 8082
FOLDER = "../Session-04/"
filename = FOLDER + 'FRAT1.txt'

# Create sequence
s = Seq()

# Read the file
s.read_fasta(filename)

# Creating fragments of length 10
frag1 = "Fragment 1: "
frag2 = "Fragment 2: "
frag3 = "Fragment 3: "
frag4 = "Fragment 4: "
frag5 = "Fragment 5: "
frag6 = "Fragment 6: "
frag7 = "Fragment 7: "
frag8 = "Fragment 8: "
frag9 = "Fragment 9: "
frag10 = "Fragment 10: "
fragments = [frag1, frag2, frag3, frag4, frag5,frag6, frag7, frag8, frag9, frag10]

i = 0
f = 0
while f < len(fragments):
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

# connect
c = Client(IP, PORT)
c2 = Client(IP, PORT2)

x = 0
while x < len(fragments):
    if x % 2 == 0 or x == 0:
        c.talk(fragments[x])
    else:
        c2.talk(fragments[x])

    x += 1

# Print
print("Gene FRAT1:", s)
for frag in fragments:
    print(frag)