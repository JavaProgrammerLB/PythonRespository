'''
程序随机生成一个数字不重复的四位数（如1234），
要求玩家和电脑竞猜猜出这个答案。每次玩家竞猜，
程序会以“XAXB”的形式提示玩家，其中“A”表示数字和位置都正确，
“B"表示位置不正确但数字正确，“X”表示相应的个数，电脑在XAXB中列出所有的结果集
'''
import random

def main():
    print('计算机随机产生的一个数字不重复的四位数为：****')
    l = random.sample(list(range(10)),4)
    print(l)
    print('游戏开始：')
    while(True):
        s = input('输入一个数字不重复的四位数：')
        try:
            i = int(s)
            if i == 0 :
                print('【输入错误】输入的数字有重复')
            else:
                d = i % 10
                c = ((i - d) % 100) / 10
                b = ((i - d - c * 10) % 1000) / 100
                a = (i - d - c * 10 - b * 100) / 1000
                if a != 0 and (i / 1000 > 9.999 or i / 1000 < 0.999):
                    print('【输入错误】输入的数字不为4')
                elif a == b or a == c or a == d or b == c or b == d or c == d:
                    print('【输入错误】输入的数字有重复')
                elif a == 0 and (i / 100 > 9.999 or i / 100 < 0.999):
                    print('【输入错误】输入的数字不为4')
                else:
                    result = check(l,a,b,c,d)
                    if result == 4:
                        print('【胜利】')
                        break
        except ValueError:
            print('【输入错误】只能输入数字')

def check(l,a,b,c,d):
    numA = countA(l,a,b,c,d)
    numB = countB(l,a,b,c,d)
    print('判定：{numA}A{numB}B'.format(numA = numA,numB = numB))
    listResultWithNumANumB(numA,numB,a,b,c,d)
    return numA

def countA(l,a,b,c,d):
    countA = 0
    if(l[0] == a):
        countA = countA + 1
    if(l[1] == b):
        countA = countA + 1
    if(l[2] == c):
        countA = countA + 1
    if(l[3] == d):
        countA = countA + 1
    return countA

def countB(l,a,b,c,d):
    countB = 0
    if(l[0] != a and (l[1] == a or l[2] == a or l[3] == a)):
        countB = countB + 1
    if(b != l[1] and (b == l[0] or b == l[2] or b == l[3])):
        countB = countB + 1
    if(c != l[2] and (c == l[0] or c == l[1] or c == l[3])):
        countB = countB + 1
    if(d != l[3] and (d == l[0] or d == l[1] or d == l[2])):
        countB = countB + 1
    return countB

def listResultWithNumANumB(numA,numB,a,b,c,d):
    if numB == 4:
        print('可能的结果为： ' )
        print('{} '.format(makeANum(b,a,d,c)))
        print('{} '.format(makeANum(b,c,d,a)))
        print('{} '.format(makeANum(b,d,a,c)))
        print('{} '.format(makeANum(c,a,d,b)))
        print('{} '.format(makeANum(c,d,a,b)))
        print('{} '.format(makeANum(c,d,b,a)))
        print('{} '.format(makeANum(d,a,b,c)))
        print('{} '.format(makeANum(d,c,a,b)))
        print('{} '.format(makeANum(d,c,b,a)))

#根据四个[0-9]构造一个四位数字
def makeANum(a,b,c,d):
    return int(a * 1000 + b * 100 + c * 10 + d)

if __name__ == '__main__':
    main()
