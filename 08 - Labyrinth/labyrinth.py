import telnetlib
import getch

HOST = '52.49.91.111'
PORT = 1986

tn = telnetlib.Telnet(HOST, PORT)
print tn.read_until('asdf', timeout=.1)

# Let's play labyrinth!
while True:
    char = getch.getch()
    if char == 's':
        tn.write(chr(100) + '\n')
    elif char == 'a':
        tn.write(chr(108) + '\n')
    elif char == 'd':
        tn.write(chr(114) + '\n')
    elif char == 'w':
        tn.write(chr(117) + '\n')

    print tn.read_until('asdf', timeout=.1)
