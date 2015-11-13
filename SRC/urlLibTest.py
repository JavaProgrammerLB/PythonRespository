import json
import urllib.request

def main():
    print('hello')
    with urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US') as f:
        s = f.read(10000).decode('utf-8')
        print(s)
        print(type(s))
        dictO= json.loads(s)
        print(dictO)
        print(type(dictO))
        images = dictO['images']
        print(images)
        print(type(images))
        for i in range(len(images)):
            print(images[i]
        
if __name__ == '__main__':
    main()