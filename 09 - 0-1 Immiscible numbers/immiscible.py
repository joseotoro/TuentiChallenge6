import re
import math
pattern = re.compile('0')


def is_01_immiscible(n):
    ones = False
    while n > 0:
        digit = n % 10
        n /= 10
        if digit == 0:
            if ones:
                return False
        elif digit == 1:
            ones = True
        else:
            return False
    return True


def get_digits(n):
    ones = int(math.log10(n)) + 1
    zeros = 0
    while n > 0:
        digit = n % 10
        n /= 10
        if digit == 0:
            zeros += 1
            ones -= 1
        else:
            break
    return ones, zeros


def primes(n):
    primfac = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

with open('submitInput', 'rb') as f:
    lines = f.readlines()
    lines = map(lambda x: x.replace('\n', ''), lines)

with open('out.txt', 'wb') as out:
    for case, num in enumerate(lines):
        if case != 0:
            print str(case) + ' / ' + lines[0] + ' (' + num + ')'
            number = int(num)
            if is_01_immiscible(number):
                ones_multiples, zeros = get_digits(number)
                out.write('Case #' + str(case) + ': ' +
                          str(ones_multiples) + ' ' + str(zeros) + '\n')
            else:
                # http://math.stackexchange.com/questions/164986/smallest-multiple-whose-digits-are-only-ones-and-zeros
                pr = primes(number)
                twos = pr.count(2)
                threes = pr.count(3)
                fives = pr.count(5)
                zeros_in_number = max(twos, fives)
                ones_count = pow(3, threes)
                ones_total = ones_count

                one_multiples = '1' * ones_count
                test = int(one_multiples + ('0' * zeros_in_number))
                factor = pow(10, ones_count)
                ones_modulo = int(one_multiples) * pow(10, zeros_in_number)
                ones_modulo %= number

                found = False
                test %= number
                while not found:
                    if test == 0:
                        out.write('Case #' + str(case) + ': ' +
                                  str(ones_total) + ' ' +
                                  str(zeros_in_number) + '\n')
                        found = True
                    else:
                        test = (test * factor + ones_modulo) % number
                        ones_total += ones_count
