from collections import Counter
import telnetlib

# Read words
with open('words.txt', 'rb') as f:
    w = f.readlines()
    w = map(lambda x: x[:-2], w)

HOST = '52.49.91.111'
PORT = 9988

# Connect to hangman service
tn = telnetlib.Telnet(HOST, PORT)
tn.read_until('continue...')
tn.write('\n')

length = 0
letters = set()

# Automatic hangman player!
while True:
    z = tn.read_until('level', timeout=.2)
    print z
    if "next level" in z:
        key = filter(lambda x: ":" in x, z.split('\n'))
        if key:
            key = key[0].split(':')[1].strip()
            print 'key: ' + key
        tn.write('\n')
        z = tn.read_until('level', timeout=.2)

    z = z.split('\n')
    word = ''.join(z[-3].split())

    if length != len(word):
        length = len(word)
        letters = set()
        words = filter(lambda x: len(x) == length, w)

    indexes = []
    for index, letter in enumerate(word):
        if letter == '_':
            indexes.append(index)
        else:
            words = filter(lambda x: x[index] == letter, words)

    more_probable_letter = [x[i] for x in words for i in indexes
                            if x[i] not in letters]
    letter = Counter(more_probable_letter).most_common(1)[0][0]
    letters.add(letter)
    tn.write(letter + '\n')
