moves = {}
transitions = {}
writes = {}
tapes = []

# Like a Turing machine!
with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()[2:]
    lines = lines[:-1]
    tapes_sec = False
    current_state = ''
    current_char = ''
    for line in lines:
        if not tapes_sec:
            # move, transition or write
            if line.startswith('      '):
                l = line.split(':')
                instruction = l[0].strip()
                if instruction == 'write':
                    character = l[1].split('\'')[1]
                    writes[(current_state, current_char)] = character
                elif instruction == 'move':
                    if l[1].strip() == 'left':
                        move = -1
                    else:
                        move = 1
                    moves[(current_state, current_char)] = move
                elif instruction == 'state':
                    transitions[(current_state, current_char)] = l[1].strip()
            # char
            elif line.startswith('    '):
                current_char = line.split('\'')[1]
            # state
            elif line.startswith('  '):
                current_state = line.strip()[:-1]
            # tapes
            else:
                tapes_sec = True
        else:
            tapes.append(line.split('\'')[1])

with open('output.txt', 'wb') as out:
    for case, _tape in enumerate(tapes):
        tape = list(_tape)
        state = 'start'
        index = 0
        while state != 'end':
            if index == len(tape):
                tape.append(' ')
            if index == -1:
                tape.insert(0, ' ')
                index = 0
            char = tape[index]
            config = (state, char)
            if config in writes:
                tape[index] = writes[config]
            if config in moves:
                index += moves[config]
            if config in transitions:
                state = transitions[config]
        out.write('Tape #' + str(case + 1) + ': ' + ''.join(tape) + '\n')
