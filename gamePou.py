import random

#hunger = [0,1,2,3,4,5,6,7,8,9,10]
#energy = [0,1,2,3,4,5,6,7,8,9,10]
#happiness = [0,1,2,3,4,5,6,7,8,9,10]
#health = [0,1,2,3,4,5,6,7,8,9,10]
#age = [1,2,3]


class Pou:

    def __init__(self, name, age, hunger, energy, happiness, health, status):
        self.name = name
        self.age = age 
        self.hunger= hunger 
        self.energy= energy 
        self.happiness= happiness
        self.health= health 
        self.alive = True
        
        
    def play(self):
        self.hunger -= 1
        self.energy -= 2
        self.health += 1
        if(self.energy <=5):
            self.happiness -= 1
        else:
            self.happiness += 5
        print(self.status)

    def eat(self):
        self.hunger += 5
        self.energy -= 1
        self.happiness +=1
        self.health += 2
        print(self.status)
    
    def sleep(self):
        self.hunger -= 1
        self.energy += 5
        self.happiness +=1
        self.health += 2
        print(self.status)

        
    def status(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Hunger: ", self.hunger)
        print("Energy: ", self.energy)
        print("Happiness: ", self.happiness)
        print("Helth: ", self.health)


coco = Pou("coco",random.randint(1,3), random.randint(0,10), random.randint(0,10), random.randint(0,10),random.randint(0,10),random.randint(0,10))
print()


while True:
    print("What do you want to do?")
    print("Eat")
    print("Sleep")
    print("Play")
    print("Show status")
    print("Exit")
    option = input()
    if option == "Eat":
        coco.eat()
    elif option == "Sleep":
        coco.sleep()
    elif option == "Pay":
        coco.play()
    elif option == "Show status":
        coco.status()
    elif option == "Exit":
        break
    else:
        print("What do you want to do?")