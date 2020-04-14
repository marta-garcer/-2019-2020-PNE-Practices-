from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "10.3.33.54"
PORT = 8086
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
fragments = [frag1, frag2, frag3, frag4, frag5]

i = 0
f = 0
while f < 5:
    sequence = str(s)
    fragments[f] += sequence[i]
    i += 1
    if i % 10 == 0:
        f += 1

# connect
c = Client(IP, PORT)

c.talk(fragments[0])
c.talk(fragments[1])
c.talk(fragments[2])
c.talk(fragments[3])
c.talk(fragments[4])

# Print
print("Gene FRAT1:", s)
for frag in fragments:
    print(frag)