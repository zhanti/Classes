class Student:
    def __init__(self):
        self.__name = None
        self.__surname = None
        self.__age = None

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def surname(self):
        return self.__surname
        
    @surname.setter
    def surname(self,surname):
        self.__surname = surname
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age = age
    
    def showInfo(self):
        print(self.name)
        print(self.surname)
        print(self.age)