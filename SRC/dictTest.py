
def main():
    d = dict()
    d['.java'] = 1
    print(d)
    print('.java' in d)

    d1 = {'one0':1,'two0':2,"three0":3}
    print(d1,type(d1))

    d2 = dict(one1 = 1,two1 = 2, three1 = 3, four1 = 4 )
    print(d2,type(d2))

    for k,v in d2.items():
        print(k,v)

    d3 = dict(**d,**d1,**d2)
    print(d3,type(d3))

    print(d3.get('one'))
    print(d3.get('one','not found, liubei ni zhen shuai'))
    print(d3.get('one0'))
    print(d3,type(d3))
    print(d3.pop('one1'))

    print('-------------')
    print(d3['two1'])
if __name__ == '__main__':
     main()
