import socket
from threading import Thread

HOST = '0.0.0.0'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

def handle_client():
	conn, addr = s.accept()
	print 'Connected by', addr

	while 1:

		data = conn.recv(1024)
		if not data: break

		print data

		conn.sendall(data)

	conn.close()

print 'Listening at', (HOST, PORT), '...'

for i in range(10):
	Thread(target=handle_client).start()

s.close()

