from Seq0 import *

FOLDER = "../Session-04 folder/"
genes = ['U5', 'ADA', 'FRAT1','FXN']

for file in genes:
    sequence = seq_read_fasta(FOLDER + file + '.txt')
    print("Gene " + file + "---> Length:", seq_len(sequence))
