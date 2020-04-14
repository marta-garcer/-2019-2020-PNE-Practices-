import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.124.179"

while True:
  # -- Ask the user for the message
  message = input("Enter the message that you want to send: ")

  # -- Create the socketç
# We will always use this parameters: AF_INET (connected to internet) y SOCK_STREAM
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # -- Establish the connection to the Server
  s.connect((IP, PORT))

  # -- Send the user message
  msg_sent = str.encode(message)
  s.send(msg_sent)


  # -- Close socket
  s.close()