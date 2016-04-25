import getpass
import telnetlib
import os

def main():
    u ="root"
    p ="linux"
    h='192.168.1.248'
    connectHost(h,u,p)

def connectHost(Host,user,password):
    try :
        tn = telnetlib.Telnet(Host)

        tn.read_until(b"login: ")
        tn.write(user.encode('utf-8') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('utf-8') + b"\n")
            print('登录成功')
            # print(os.environ)
            tn.write(b"ls\n")
            tn.write(b"cd nand\n")
            tn.write(b"ls\n")
            # tn.write(b"vi term.ini.good")
            tn.write(b"exit\n")
            print(tn.read_all().decode('utf-8'))
        else:
            print('登录失败')

        tn.write(b"ls\n")
        #tn.write(b"cd nand\n")
        #tn.write(b"ls\n")
        tn.write(b"exit\n")
        #print(tn.read_all().decode('utf-8'))
        print("{} telnet成功连接".format(Host))
        return 1
    except TimeoutError:
        print("{} telnet连接失败".format(Host))
        return 0
    except ConnectionRefusedError:
        print("{} telnet连接失败".format(Host))
        return 0
    except ConnectionResetError:
        print("{} telnet连接失败".format(Host))
        return 0
    except OSError:
        print("{} telnet连接失败".format(Host))
        return 0

if __name__ == '__main__':
    main()
