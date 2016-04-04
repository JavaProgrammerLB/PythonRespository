import webbrowser as w
import string

#探索规则:字母表
def exploreWithAscciiLetterPlusTopLevelDomain():
    b = w.get('open -a Google\ Chrome.app %s ' )
    # b.open('https://www.baidu.com',0)
    strli = getStr()
    doma = getTopLevelDomain('cn','com','net','org','fi')
    for i in range(len(strli)):
        for j in range(len(doma)):
            b.open("http://www.{}.{}".format(strli[i],doma[j]),1,True)

#自定义探索规则
def exCustome():
    b = w.get('open -a Google\ Chrome.app %s ' )
    # domain = parseStr2Set('girl','beauty')
    # domain = parseStr2Set('home','love','hard','friend','color','fire','school','hot')
    # domain = parseStr2Set('red','bed','sheet','refrigerator','oven','ice','egg','sea')
    # s = 'flower'
    # domain = ('apple','orange','bread')
    #domain = ('paper','news')
    #domain = ('one','two','three','four','five','six','seven','eight','nine','ten')
    # domain = ('explore',)
    # domain = ('dog','cat','snake')
    # domain = ('coder',)
    #domain = ('linus',)
    # domain = ("laugh",)
    # domain = ('car','music')
    # domain = ('movie','mp3')
    # domain = ('beautiful','card','police')
    # domain = ('milk','rice','baby')
    # domain = ('like','')
    # domain = ('jinmao',)
    # domain = ('bird','ymc','dog','jinmao')
    # domain = ('map','picture','skin','jump','go','play','ground')
    # domain = ('command','code','web')
    # domain=('a',)
    # domain = ('meinv','beautiful','women','girl','beauty','haokan','pretty','nvhai')
    # domain = ('joke','kidding','xiao','smile')
    # domain = ('as','person')
    # domain = ("book",'music','love','happy','honest')
    domain = ('sing','dance','work','study')
    topDomain = parseStr2Set('cn','com','de','net','org','fi','no','me','jp','io','co.jp','edu')
    explore(domain,topDomain)
    # exploreWithNum(topDomain)
    # domain = ('chifan','kuaile','xiangfa','wufazhuce','yitianyigexiangfa','shuiguo','meinv')
    # domain = ('hua','pifu','huazhuang','pianyi','meili','wanzheng','youxiu','ren')
    # domain = ('fangzi','shu','tupian','youmo','shuijiao')
    # domain = ('shouji','shijian','didian','ditu','shui','shiwu','shenghuo')
    # domain = ('huaping','meigui','yu','chitang')
    # exploreChinesePinyin(domain)

#探索由汉语拼音组成的url
def exploreChinesePinyin(domain):
    topDomain = ('cn','com','org','net')
    b = w.get('open -a Google\ Chrome.app %s')
    for i in range(len(domain)):
        for j in range(len(topDomain)):
            b.open("http://www.{}.{}".format(domain[i],topDomain[j]))


#domain为1到10的整数
def exploreWithNum(topDomain):
    b = w.get('open -a Google\ Chrome.app %s')
    for i in range(10):
        for j in range(len(topDomain)):
            b.open("http://www.{}.{}".format(i,topDomain[j]),1,True)

#domain和topDomain为两个set
def explore(domain,topDomain):
    b = w.get('open -a Google\ Chrome.app %s ' )
    for i in range(len(domain)):
        for j in range(len(topDomain)):
            b.open("http://www.{}.{}".format(domain[i],topDomain[j]),1,True)
    print('共打开{}个网站'.format(len(domain)*len(topDomain)))


#获取二十六个字母,以list返回
def getStr():
    s = string.ascii_letters
    l = list()
    for i in range(26):
        l.append(s[i:i+1])
    return l

#获取二十六个字母的第二种方式,返回的是（'abcdefghijklmnopqrstuvwxyz'）
#注意:只含有一个元素的set的相关问题（'abcdefghijklmnopqrstuvwxyz',）
def getStr2():
    le = string.ascii_lowercase
    se = (le)
    return se

#保存有趣的网址
def getUrl():
    url = ('o.de','p.de')
    #基本上a-z的.org都在出售

#定义顶级域名set
def getTopLevelDomain(*args):
    #常用的顶级域名保存:.cn .com .org .net .edu
    # *args 为一个set
    return args
    #set里面只有一个元素的时候,在第一个元素后面要加上一个逗号
    # s=('com',)

#讲string转化成一个set返回
def parseStr2Set(*args):
    return args

if __name__ == '__main__':
    #根据字母表探索
    # exploreWithAscciiLetterPlusTopLevelDomain()
    #自定义探索
    exCustome()