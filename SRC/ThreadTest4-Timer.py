from threading import Timer
def hello():
    print('hello timer')

t = Timer(30,hello)
t.start()
