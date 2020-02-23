from Seq0 import *
print('-----| Exercise 5 |------')

folder = "../Session-04 folder/"
bases = [ 'A', 'C', 'T', 'G']
genes = ['U5', 'ADA', 'FRAT1','FXN', 'RNU6_269P']

for file in genes:
    sequence = seq_read_fasta(folder + file + '.txt')
    print('Gene ' + file, seq_count(sequence))