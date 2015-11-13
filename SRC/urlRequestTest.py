import urllib.request

with urllib.request.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US') as f:
    s=f.read(30000).decode('GB2312','ignore')
    file = open('urlRequstTest.txt','w')
    file.write(str(s))
    file.close()
