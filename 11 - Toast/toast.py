def toast(x, m):
    if x < 0 or k % m != 0:
        return 'IMPOSSIBLE'
    m = set([m])
    total = 0
    while x != 0:
        biggest = max(m)
        if biggest <= x:
            x -= biggest
            m.add(biggest * 2)
        else:
            x -= max(filter(lambda y: y <= x, m))
        total += 1
    return str(total)

with open('submitInput', 'rb') as f:
    lines = f.readlines()
    lines = map(lambda x: x.replace('\n', ''), lines)

with open('output.txt', 'wb') as out:
    for case, config in enumerate(lines):
        if case != 0:
            print 'Case ' + str(case)
            n, m, k = map(lambda x: int(x), config.split())
            table = [m for _ in range(n)]
            result = toast(k - n * m, m)
            out.write('Case #' + str(case) + ': ' + result + '\n')
