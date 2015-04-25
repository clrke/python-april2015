# Echo client program
import socket

HOST = '0.0.0.0'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	reply = raw_input("Chat (type 'x' to exit):")
	if reply == 'x':
		break

	s.sendall(reply)
	data = s.recv(1024)

	print data

s.sendall('Good bye!')

s.close()
