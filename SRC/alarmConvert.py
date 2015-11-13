import re

def main():
    oldFileName = input('Enter the oldFileName:')
    newFileName = input('Enter the newFileName:')
    printConvert(oldFileName,newFileName)

def printConvert(oldFileName,newFileName):
    file_alarm = open(oldFileName)
    list_alarm = file_alarm.readlines() #file_alarm.readlines() return a list
    #open
    newFile = open(newFileName,'w')
    #loop
    for lineStr in list_alarm:
        #match
        regString = r'\bprint[a-z]*'
        s = re.findall(regString,lineStr)
        pat = re.compile(regString)
        if pat.search(lineStr):
            lineStr = lineStr[0:len(lineStr)-1]
            lineStr += ')\n'
        lineStr = lineStr.replace('print ','print(')
        #write
        newFile.write(lineStr)
    #close
    newFile.close()

if __name__ == '__main__':
    main()
