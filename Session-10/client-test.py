from Client0 import Client
import termcolor

IP = "192.168.1.58"
PORT = 8080

for i in range(5):

    c = Client(IP, PORT)

    print('To Server: ', end="")
    termcolor.cprint(f"Message {i}", 'blue')
    print('From Server: ', end="")
    termcolor.cprint(c.debug_talk(f"ECHO: Message {i}"))