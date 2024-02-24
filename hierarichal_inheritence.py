class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Dog(Animal):
    def __init__(self, name, age,sound):
        super().__init__(name, age)
        self.sound = sound

    def show(self):
        super().show()
        print(f"Sound: {self.sound}")

class Cat(Animal):
    def __init__(self,name,age,sound,child):
        super().__init__(name,age)
        self.child = child
        self.sound = sound

    def show(self):
        super().show()
        print(f"Sound: {self.sound}")
        print(f"Child: {self.child}")

class GermanShaperd(Dog):
    def __init__(self, name, age, sound,price):
        super().__init__(name, age, sound)
        self.price = price

    def show(self):
        super().show()
        print(f"Price: {self.price}")

class Meow(Cat):
    def __init__(self, name, age, sound, child,food):
        super().__init__(name, age, sound, child)
        self.food = food

    def show(self):
        super().show()
        print(f"Food: {self.price}")

class Persian(Dog):
    def __init__(self, name, age, sound, cut):
        super().__init__(name, age, sound)
        self.cut = cut

    def show(self):
        super().show()
        print(f"Cut: {self.cut}")

class Billow(Cat):
    def __init__(self, name, age, sound, child, smile):
        super().__init__(name, age, sound, child)
        self.smile = smile

    def show(self):
        super().show()
        print(f"Smile: {self.smile}")

billi = Billow("Billo",5,"Meow Meow",3,"Cute")
billi.show()

print()

pers = Persian("Persian",6,"Bark","Very Dangerous")
pers.show()