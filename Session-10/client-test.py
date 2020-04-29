from Client0 import Client
import termcolor

IP =  "192.168.1.37"
PORT = 8081

for index  in range(5):

    c = Client(IP, PORT)
    c.debug_talk(f"Message {index}")

