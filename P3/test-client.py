from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters
IP = "127.0.0.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
sequence_test = "TGTGAACATTCTGCACAGGTCTCTGGCTGCGCCTGGGCGGGTTTCTT"

print("Connection to SERVER at", IP, ", PORT: ", PORT)

# PING
print("* Testing PING...")
print(c.talk("PING"))

# TEST GET
print("\n* Testing GET...")
for i in range(5):
    test = f"GET {i}"
    print(f"{test}: {c.talk(test)}")

# INFO
print("* Testing INFO...")
print(c.talk("INFO " + sequence_test))

# TEST COMP
print("\n* Testing COMP...")
print("COMP " + sequence_test)
print(c.talk("COMP " + sequence_test))

# TEST REV
print("\n* Testing REV...")
print("REV " + sequence_test)
print(c.talk("REV " + sequence_test))

# TEST GENE
print("* Testing GENE...")
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in files_list:
    print("\nGENE", file)
    print(c.talk("GENE " + file))