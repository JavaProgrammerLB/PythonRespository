def main():
    #s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
    s = 'map'
    for c in s:
        if c == 'y':
            c = 'a'
        elif c == 'z':
            c = 'b'
        elif c == '\'':
            pass
        elif c== ' ':
            pass
        elif c=='.':
            pass
        elif c=='(':
            pass
        elif c==')':
            pass
        else:
            c = chr(ord(c) + 2)
        print(c,end='')

if __name__ == '__main__':
    main()
