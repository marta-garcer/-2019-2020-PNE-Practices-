from Seq0 import *

FOLDER = "../Session-04 folder/"
genes = ['U5', 'ADA', 'FRAT1','FXN']

print("-----| Exercise 3 |------")
for file in genes:
    sequence = seq_read_fasta(FOLDER + file + '.txt')
    print("Gene " + file + "---> Length:", seq_len(sequence))
