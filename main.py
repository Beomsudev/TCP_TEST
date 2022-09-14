import socket
import binascii
import time


a = b"LON\r"
print(a)
print(type(a))

s = socket.socket()
s.connect(('169.254.0.2', 9004))
s.settimeout(2000)
s.send(b"LON\r")
time.sleep(2)
s.send(b"LOFF\r")

print(s.recv(1024).decode('utf-8'))
s.close()