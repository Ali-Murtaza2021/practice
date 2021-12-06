class Animal(object):
    health="good"
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def description(self):
        print (self.name)
        print (self.age)

hippo=Animal("George","12")
print (hippo.description())

sloth=Animal("Mani","7")
ocelot=Animal("Prince","2")

print ("sloth health:",sloth.health)
print ("ocelot health:", ocelot.health)
print ("hippo health:", hippo.health)