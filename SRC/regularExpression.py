import sys,re
pat = re.compile('print')
print(type(pat))

while 1:
    line = input('Enter a line ("q" to quit):')
    if line == 'q':
        break
    if pat.search(line):
        print( 'matched:', line)
    else:
        print ('no match:', line)
