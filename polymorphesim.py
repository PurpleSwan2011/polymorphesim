class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat.My name is{self.name} my age is{self.age} years old")
    def makesound(self):
        print("meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a dog.My name is{self.name} my age is{self.age} years old")
    def makesound(self):
        print("bark")
Cat1 = Cat("dodo",8.5)
Dog1 = Dog("bubble",7)
for animal in(Cat1,Dog1):
    animal.makesound()
    animal.info()
    
