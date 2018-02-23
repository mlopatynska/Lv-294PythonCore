class Creature:
    def __init__ (self, name):
        self.name = (name)
    def __repr__(self):
        return "I'm {}".format(self.name)
    def __del__(self):
        print "{}: I'll be back!".format(self.name)
    def talk (self):
        print "I am {}. I can talk!".format(self.name)
    def breathe(self):
        print "I can breathe!"
    def move (self):
        print "{}: I can move!".format(self.name)

class Animal(Creature):
    def __init__ (self, name, sound, food, legs = 4):
        self.name = name
        self.sound = sound
        self.lags = legs
        self.food = food
    def talk(self):
        print "{}: I can make sound '{}'!".format(self.name, self.sound)
    def eat(self):
        print "{} I like {}".format(self.name, self.food)
    def __add__ (self, other):
        return Animal(self.name + other.name, self.sound + other.sound, "Everything", self.legs + self.legs )
    def __repr__ (self):
        return "I am {}. I make {}. I like {} and have {} lags.",format (self.name, self.sound, self.food, self.legs)
class Human(Creature):
        pass

class Alien(Creature):
        pass

animal = Creature("Animal")
human = Creature("Human")
alien = Creature("Alien")


sheep = Animal("Dolly", "beee", "grass")
farmer = Human("Ivan")
dog = Animal ("Tuzik", "Woof!", "meat")

#
animal.talk()
# Human.move()
# Alien.breathe()
#
# del Alien
sheep.move()
sheep.talk()
farmer.talk()
sheep.eat()
dog.eat ()

m = sheep + dog
print m
#
input ("Do you want to quit?")