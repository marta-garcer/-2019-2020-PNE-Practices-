class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        bases = ['A', 'C', 'T', 'G']
        for i in strbases:
            if i not in bases:
                print("ERROR!!")
                self.strbases = "INCORRECT sequence detected"
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")