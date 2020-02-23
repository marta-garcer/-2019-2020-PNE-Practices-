from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
bases = ['A', 'C', 'T', 'G']

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print("\tBases: ", s1.count())
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print("\tBases: ", s2.count())
print(f"Sequence 3: (Length: {s3.len()}) {s3}")
print("\tBases: ", s3.count())