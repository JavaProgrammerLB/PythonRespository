class Person:
    population = 0
    
    def __init__(self,name):
        self.name = name
        print("Initialing %s"% self.name)
        Person.population += 1
        
    def __del__(self):
        print("%s say Goodbye"% self.name)
        self.__class__.population -= 1
        
        if self.__class__.population == 0 :
            print("i am the last one")
        else :
            print("there are still %d person"% self.__class__.population)
    
    def sayHi(self):
        print("hi, my name is %s"% self.name)
    
    def howMany(self):
        if Person.population == 0 :
            print("i am the last one here")
        else :
            print(" we have still %d person here"% Person.population)
            
            
liubei = Person("liubei")
liubei.sayHi()
liubei.howMany()

xiaoyuan = Person("yuanmengchen")
xiaoyuan.sayHi()
xiaoyuan.howMany()

liubei.sayHi()
liubei.howMany()

