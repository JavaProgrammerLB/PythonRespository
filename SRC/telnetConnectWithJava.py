import telnetlib
import time

def main():
    tn = telnetlib.Telnet('192.168.1.68',8005)
    while True:
        s = input('what do you want to talk to java,type q for quit >>>')
        time.sleep(10)
        print('liubei start')
        tn.write(s)

if __name__ == '__main__':
    main()
