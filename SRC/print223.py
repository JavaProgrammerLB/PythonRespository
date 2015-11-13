def main():
    alarmPy = open("alarm.py")
    for i in alarmPy.readlines():
        print(type(i))
        break

if __name__ == '__main__':
    main()
