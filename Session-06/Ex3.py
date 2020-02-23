class Seq:
    def __init__(self, strbases):
        bases = ["A", 'C', 'G', 'T']
        for b in strbases:
            if b not in bases:
                print("ERROR!")
                self.strbases = "INCORRECT sequence detected"
                return

        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
        for seq in seq_list:
            print(f"Sequence {seq_list.index(seq)}: (Length: {seq.len()}) {seq}")


def generate_seqs(pattern, number):

    sequences = []

    for i in range(1, number + 1):
        sequences.append(Seq(pattern * i))
    return sequences

#- - Main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)