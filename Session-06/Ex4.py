import termcolor

class Seq:
    def __init__(self, strbases):
        bases = ["A", 'C', 'G', 'T']
        for i in strbases:
            if i not in bases:
                print("ERROR!")
                self.strbases = "INCORRECT sequence detected"
                return

        self.strbases = strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(seq_list, color):
    for seq in seq_list:
        termcolor.cprint(f"Sequence {seq_list.index(seq)}: (Length: {seq.len()}) {seq}", color)


def generate_seqs(pattern, number):

    sequences = []

    for i in range(1, number + 1):
        sequences.append(Seq(pattern * i))
    return sequences


#- - Main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()
termcolor.cprint("List 2:",  'green')
print_seqs(seq_list2, 'green')