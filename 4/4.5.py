class Animal:
    def breathe(self):
        pass
    def eat(self):
        pass
class Fish(Animal):
    def swim(self):
        pass
class Bird(Animal):
    def lay_eggs(self):
        pass
class FlyingBird(Bird):
    def fly(self):
        pass
# использование классов
fish = Fish()
fish.swim()
bird = Bird()
bird.eat()
bird.lay_eggs()
flying_bird = FlyingBird()
flying_bird.breathe()
flying_bird.fly()