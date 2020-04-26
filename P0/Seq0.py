from pathlib import Path


def seq_ping():
    print('OK!')



def seq_read_fasta(filename):
    file_contents = Path(filename).read_text().split('\n')[1:]
    new_file = "".join(file_contents)
    return new_file


def seq_len(seq):
    return (len(seq))


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    bases = ['A', 'C', 'T', 'G']
    count_bases = []
    for base in bases:
        count_bases.append(seq_count_base(seq, base))
    dicti = dict(zip(bases, count_bases))
    return dicti


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(seq):
    bases = ['A', 'C', 'T', 'G']
    compl_bases = ['T', 'G', 'A', 'C']
    dict_bases_compl = dict(zip(bases, compl_bases))
    complementary = ''
    for i in seq:
        for base, c_base in dict_bases_compl.items():
            if i == base:
                complementary += c_base
    return(complementary)