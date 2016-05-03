import operator

with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()

# Read manuscript
with open('corpus.txt', 'rb') as f:
    words = f.readlines()[0].split()

with open('output.txt', 'wb') as out:
    for case, inp in enumerate(lines):
        if case != 0:
            indexes = inp.split()
            a = int(indexes[0]) - 1
            b = int(indexes[1])

            # Count the frequency of words
            word_count = {}
            for i in range(a, b):
                if words[i] in word_count:
                    word_count[words[i]] += 1
                else:
                    word_count[words[i]] = 1

            # Sort by frequencies
            sorted_words = sorted(word_count.items(),
                                  key=operator.itemgetter(1))

            out.write('Case #' + str(case) + ': ')
            (key, value) = sorted_words[-1]
            out.write(key + ' ' + str(value) + ',')
            (key, value) = sorted_words[-2]
            out.write(key + ' ' + str(value) + ',')
            (key, value) = sorted_words[-3]
            out.write(key + ' ' + str(value) + '\n')
