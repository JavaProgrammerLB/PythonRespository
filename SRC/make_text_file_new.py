'make_text_file.py  -----  create text file by xiaoyuan'

import os
ls = os.linesep

while True:
    if os.path.exists(fname):
        print("ERROR:'%s' already exists" % fname)
    else:
        break

#get file content lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

#loop until user terminates input
while Ture:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print('DONE!')
