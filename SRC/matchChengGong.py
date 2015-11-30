import sys,re

def main():
    pat = re.compile('成功')
    print(type(pat))

    file = open('telnetResult.txt')
    count = 0
    for line in file.readlines():
        if pat.search(line):
            print('{}'.format(line),end='')
            count = count + 1
    else:
        print('共{}个ip tlenet连接成功'.format(count))

if __name__ == '__main__':
    main()
