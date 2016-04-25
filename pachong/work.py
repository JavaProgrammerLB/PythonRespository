import re

def main():
    # f = open('source.txt','r',errors="ignore")
    # for line in f.readlines():
    #     m = re.search('^(http)(s)?(\:\/\/img9\.ph\.126\.net)([^ ]*)$',line)

    s = '<DIV align="center"  ><A target="_blank" href="http://ljzlcl.blog.163.com/"  ><IMG style="margin: 0px;"   title="王羲之《兰亭序》冯摹高清晰单字版 - 無為居士 - 聚美齋"   alt="王羲之《兰亭序》冯摹高清晰单字版 - 無為居士 - 聚美齋"   src="http://img9.ph.126.net/S_mHcu7B4VSuLA5b5hIsDA==/2646990681004049139.jpg"   ></A></DIV>'
    print(re.search('^(http)(s)?(\:\/\/img9\.ph\.126\.net)([^ ]*)$',s))

if __name__ == '__main__':
    main()
