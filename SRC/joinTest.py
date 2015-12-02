
def main():
    a = 'abcd'
    aList = ['a','b','c','d']
    aTuple = ('a','b','c')
    aMap = {'a':1,'b':2,'c':3}
    joinThing(a)
    joinThing(aList)
    joinThing(aTuple)
    joinThing(aMap)

def joinThing(thing):
    print(','.join(thing))
    print(''.join(thing))
    print('-------------')

if __name__ == '__main__':
    main()
