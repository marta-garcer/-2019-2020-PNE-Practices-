seq_dna = input ("Introduce the sequence: ")
print ("Total length: ", len(seq_dna))
A = 0
C = 0
T = 0
G = 0

for letter in seq_dna :
    if letter == 'A' :
        A += 1
    if letter == 'T' :
        T += 1
    if letter == 'C' :
        C += 1
    if letter == 'G' :
        G += 1

print ('A =', A)
print ('T =', T)
print ('C =', C)
print ('G =', G)
