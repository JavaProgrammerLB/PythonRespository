import urllib.request
import urllib.parse
import json
import codecs
from datetime import date
import os

def main():
    f = open('url.txt','r')
    i = 0
    for url in f.readlines():
        print(url)
        with urllib.request.urlopen(url) as dataValue:
            jpg = dataValue.read()
            DstDir = os.getcwd() + '\\'
            today = date.today()
            fileDate = date.fromordinal(today.toordinal() - i)
            FileName2 = fileDate.isoformat()
            FileNameEnd = '.jpg'
            FileName=FileName2+FileNameEnd

            #下载图片并保存在当前路径
            File = open(DstDir + FileName,'wb')
            File.write(jpg)
            print('正在下载{FileName2}'.format(FileName2 = FileName2))
            File.close()
        i = i + 1

if __name__ == '__main__':
    main()
