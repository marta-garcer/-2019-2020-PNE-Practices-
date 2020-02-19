count = 0
A = 0
T = 0
C = 0
G = 0

with open ('dna' , 'r') as f :
    for line in f :
        for letter in line :
            count += 1

            if letter == 'A' :
                A += 1
            if letter == 'C' :
                C += 1
            if letter == 'T' :
                T += 1
            if letter == 'G' :
                G += 1

print ('Total length :', count)
print ('A =', A)
print ('C =', C)
print ('T =', T)
print ('G =', G)



