from Seq0 import *
print('-----| Exercise 7 |------')
folder = "../Session-04 folder/"
filename = 'U5.txt'
sequence = seq_read_fasta(folder + filename)

print('Gene ' + filename + ':')
print('Frag ' + (sequence[:20]))
print('Comp: ' , seq_complement(sequence[:20]))