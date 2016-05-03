from math import ceil

'''
Today is our bi-weekly team lunch! This time, we're going to our favorite Indian restaurant and we want to know in advance the minimum number of tables required to seat all the team members.

All the tables are square shaped, they must always be joined in a row and there can be no more than one diner seated at each side of a table.

Input
=========================
In the first line, an integer T indicates the number of cases. Each case is described in a line with an integer N indicating the number of diners.

Output
=========================
For each case t, the output is the string Case #t: r where t is the case number and r is the result.
'''

with open('submitInput.txt', 'rb') as f:
    lines = f.readlines()

with open('output.txt', 'wb') as out:
    for case, din in enumerate(lines):
        if case != 0:
            diners = int(din)
            if diners == 0:
                out.write('Case #' + str(case) + ': 0\n')
            elif diners <= 4:
                out.write('Case #' + str(case) + ': 1\n')
            else:
                out.write('Case #' + str(case) + ': ' +
                          str(1 + int(ceil((diners - 4) / 2.0))) + '\n')

