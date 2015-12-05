def main():
    t=(1,2,3,4)
    print(t,type(t))

    t2 = 1,2,3,4,5,6,5 #,'hello' 加上'hello'之后，max(t2)会报TypeError unorderable types: str() > int()
    print(t2,type(t2))
    print('t2的长度为:{}'.format(len(t2)))
    print('t2中最大的元素为：{}'.format(max(t2)))
    print('t2中最小的元素为：{}'.format(min(t2)))
    print('t2中数字5出现的次数{}'.format(t2.count(5)))
    print('t2中数字5第一次出现的索引为{}'.format(t2.index(5)))

    t3 = tuple(range(25))
    print(t3,type(t3))
    print(23 in t3)
    print(26 not in t3)
    #t3[3] = 13 TypeError: 'tuple' object does not support item assignment
    print('t3中数字5出现的次数{}'.format(t3.count(5)))
    print('t3中数字5第一次出现的索引为{}'.format(t3.index(5)))

    t4 = range(25)
    print(t3,type(t4)) #t4的类型为： <class 'range'>



if __name__ == '__main__':
    main()
