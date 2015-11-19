import urllib.request
import urllib.error

def main():
    #url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=94485'
    #s2='and the next nothing is'
    #with urllib.request.urlopen(url) as response:
    #    result = response.read()
    #    s = result.decode()
    #    print(s)
    #    print(len(s))
    #    print(s[24:])
    #print(s[0:24].strip() == s2.strip())
    #print(s[0:24])
    #print(s2)

    url2='65520'
    s=s2='and the next nothing is'
    while (s[0:24].strip() == s2.strip()):
        url1='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
        url=url1+url2
        try:
            response = urllib.request.urlopen(url)
            result = response.read()
            s = result.decode()
            print(s)
            url2=s[24:]
        except urllib.error.URLError:
            print('here')
            response = urllib.request.urlopen(url)


if __name__ == '__main__':
    main()
