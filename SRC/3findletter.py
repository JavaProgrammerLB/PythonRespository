def main():
     file = open('3findletter.txt')
     s = file.read()
     file.close()
     for c in s[4:101247]:
         pass
     #print('hll')
     for n in range(4,len(s)-3):
         a = s[n - 3]
         b = s[n - 2]
         c = s[n - 1]
         d = s[n]
         e = s[n + 1]
         f = s[n + 2]
         g = s[n + 3]
         nd = ord(d)
         na = ord(a)
         nb = ord(b)
         nc = ord(c)
         ne = ord(e)
         nf = ord(f)
         ng = ord(g)
        if a > b:
            print(a,b,c,d,e,f,g)

     s2='1fhjkhuihuuihiuh'
    # for i in range(len(s2)):
    #     print(i,":",s2[i])


if __name__ == '__main__':
    main()
