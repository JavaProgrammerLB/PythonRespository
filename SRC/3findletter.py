def main():
     file = open('3findletter.txt')
     s = file.read()
     file.close()
     for c in s[5:101246]:
         pass

     print('start')
     for n in range(5,len(s)-4):
         aO = s[n - 4]
         a = s[n - 3]
         b = s[n - 2]
         c = s[n - 1]
         d = s[n]
         e = s[n + 1]
         f = s[n + 2]
         g = s[n + 3]
         gO = s[n + 4]
         nd = ord(d)
         na = ord(a)
         nb = ord(b)
         nc = ord(c)
         ne = ord(e)
         nf = ord(f)
         ng = ord(g)

         if sml(d) and bgl(a) and bgl(b) and bgl(c) and bgl(e) and bgl(f) and bgl(g):
            if sml(aO) and sml(gO):
                print(aO,a,b,c,d,e,f,g,gO)
            # print(a,b,c,d,e,f,g)
            #if nd == ord('l') or nd == ord('y'):
                #print(a,b,c,d,e,f,g)
            #if nb == na + 1 and nc == nb + 1:
            #    print(a,b,c,d,e,f,g)
            elif nd > na and nd > nb and nd > nc:
                pass
                 #print(a,b,c,d,e,f,g)
             #elif na == nb and nb == nc:
                 #print(a,b,c,d,e,f,g)
            # elif na == ord('E') and nb == ord('X') and nc == ord('A'):
            #     print(a,b,c,d,e,f,g)

def sml(s):
    if ord(s) >= ord('a') and ord(s) <= ord('z'):
        return True
    else:
        return False

def bgl(s):
    if ord(s) >= ord('A') and ord(s) <= ord('Z'):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
