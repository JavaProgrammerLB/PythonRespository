def main():
    foo = 'foo'
    bar = 'bar'

    foobar = '%s%s'%(foo,bar)
    print(foobar)
    foobar = '{0}{1}'.format(foo,bar)
    print(foobar)
    foobar = '{foo}{bar}'.format(foo = foo,bar = bar)
    print(foobar)

if __name__ == '__main__':
    main()
