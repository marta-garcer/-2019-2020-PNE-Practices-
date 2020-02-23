from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")
folder = "../Session-04 folder/"

bases = ['A', 'C', 'T', 'G']
genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

for file in genes:
    s = Seq()
    sequence = s.read_fasta(folder + file + ".txt")
    dict_bases = s.count()
    min_value = 0
    greater_number_base = ''
    for base, value in dict_bases.items():
        while value > min_value:
            min_value = value
            greater_number_base = base
    print('Gene ', file, ': Most frequent Base: ', greater_number_base)