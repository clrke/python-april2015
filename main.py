import socket

print(socket.gethostname())
print(socket.gethostbyname("localhost"))
print(socket.gethostbyname("google.com"))

print(socket.has_ipv6)
