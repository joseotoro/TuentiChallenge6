with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()

combos = []
combos.append(['L', 'LD', 'D', 'RD', 'R', 'P'])
combos.append(['R', 'RD', 'D', 'LD', 'L', 'K'])
combos.append(['D', 'RD', 'R', 'P'])
combos.append(['R', 'D', 'RD', 'P'])
combos.append(['D', 'LD', 'L', 'K'])


combos_miss = []
for combo in combos:
    combos_miss.append(combo[:-1])

with open('output.txt', 'wb') as out:
    for case, seq in enumerate(lines):
        if case != 0:
            count = 0
            combos_end = set()
            combo = seq.split('-')
            combo[-1] = combo[-1].replace('\r', '').replace('\n', '')
            for i in range(len(combo)):
                for j in range(len(combos)):
                    if combo[i:i + len(combos_miss[j])] == combos_miss[j] and \
                            combo[i:i + len(combos[j])] != combos[j]:
                        index_end = i + len(combos_miss[j])
                        if index_end not in combos_end:
                            count += 1
                            combos_end.add(index_end)
            out.write('Case #' + str(case) + ': ' + str(count) + '\n')
