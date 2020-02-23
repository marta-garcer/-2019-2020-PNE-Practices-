import pathlib


class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object

        if strbases == "NULL":
            print("NULL Seq created!")
            self.strbases = "NULL"
            self.length = 0

        elif strbases == "Invalid sequence":
            print("INVALID Seq!")
            self.strbases = "ERROR"
            self.length = 0

        else:
            self.strbases = strbases
            print("New sequence created!")
            self.length = len(self.strbases)

        return

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return self.length

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = ['A', 'C', 'T', 'G']
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dicti = dict(zip(bases, count_bases))
        return dicti

    def reverse(self):
        if not len(self.strbases) and not self.len():
            return self.strbases
        elif not self.len():
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if not len(self.strbases) and not self.len():
            return self.strbases
        elif not self.len():
            return self.strbases
        else:
            bases = ['A', 'C', 'T', 'G']
            compl_bases = ['T', 'G', 'A', 'C']
            dict_bases_compl = dict(zip(bases, compl_bases))
            complementary = ''
            for i in self.strbases:
                for base, c_base in dict_bases_compl.items():
                    if i == base:
                        complementary += c_base
            return complementary

    def read_fasta(self, filename):
        file_contents = pathlib.Path(filename).read_text().split('\n')[1:]
        new_file = "".join(file_contents)
        self.strbases = new_file
        self.length = len(self.strbases)