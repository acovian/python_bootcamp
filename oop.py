class Dog():

    species = 'mammal'

    def __init__(self,breed,name):

        self.breed = breed
        self.name = name

    def bark(self):
        print("WOOF My name is {}".format(self.name))

my_dog = Dog(breed='Lab', name='Frankie')

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
my_circle.pi

class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    #inherit base class
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

# mydog = Dog()
# mydog.who_am_i()

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
