import random
import time

#hunger = [0,1,2,3,4,5,6,7,8,9,10]
#energy = [0,1,2,3,4,5,6,7,8,9,10]
#happiness = [0,1,2,3,4,5,6,7,8,9,10]
#health = [0,1,2,3,4,5,6,7,8,9,10]
#age = [1,2,3]


class Pou:

    def __init__(self, name, age, hunger, energy, happiness, health, status, clean, social):
        self.name = name
        self.age = age 
        self.hunger= hunger 
        self.energy= energy 
        self.happiness= happiness
        self.health= health 
        self.clean = clean
        self.social = social
        self.alive = True
        
        
    def play(self):
        self.hunger -= 1
        self.energy -= 2
        self.health += 1
        self.clean -=1
        self.social -= 1
        if (self.happiness >=10):
            print("I don't want to play anymore.")
        if(self.energy <=5):
            self.happiness -= 1
        else:
            self.happiness += 5
        if any(value <= 2 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ\n")
        elif any(value <= 5 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ •ᴥ•ʔ\n")
        else:
            print("\n\nʕ´ᵔ ᴥᵔ`ʔ\n")
        
        print(self.status)

    def eat(self):
        self.hunger += 5
        self.energy -= 1
        self.happiness +=1
        self.health += 2
        self.clean -=3
        self.social -= 1
        if (self.hunger >=10):
            print("I don't want to eat anymore.")
        
        if any(value <= 2 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ\n")
        elif any(value <= 5 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ •ᴥ•ʔ\n")
        else:
            print("\n\nʕ´ᵔ ᴥᵔ`ʔ\n")
        
        print(self.status)
    
    def sleep(self):
        self.hunger -= 1
        self.energy += 5
        self.happiness +=1
        self.health += 2
        self.clean -=1
        self.social -= 3
        if (self.energy >=10):
            print("I don't want to sleep anymore.")
        
        if any(value <= 2 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ\n")
        elif any(value <= 5 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ •ᴥ•ʔ\n")
        else:
            print("\n\nʕ´ᵔ ᴥᵔ`ʔ\n")
        
        print(self.status)

    def cleaning(self):
        self.hunger -= 1
        self.energy -= 1
        self.happiness +=3
        self.health += 1
        self.clean +=5
        self.social -= 2
        if (self.clean >=10):
            print("I'm clean enough.")
        
        if any(value <= 2 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ")

        elif any(value <= 5 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ •ᴥ•ʔ")

        else:
            print("\n\nʕ´ᵔ ᴥᵔ`ʔ")

        
        print(self.status)

    def socialize(self):
        self.hunger -= 1
        self.energy -= 1
        self.happiness +=2
        self.health -= 1
        self.clean -=1
        self.social += 5
        if (self.social >=10):
            print("I've had enough social life.")
        
        if any(value <= 2 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ ´•̥̥̥ ᴥ•̥̥̥`ʔ")

        elif any(value <= 5 for value in (self.energy, self.hunger, self.health, self.clean, self.happiness, self.social)):
            print("\n\nʕ •ᴥ•ʔ")

        else:
            print("\n\nʕ´ᵔ ᴥᵔ`ʔ")

        
        print(self.status)

    def aging(self):
        self.age +=1

        
    def status(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Hunger: ", self.hunger)
        print("Energy: ", self.energy)
        print("Happiness: ", self.happiness)
        print("Health: ", self.health)
        print("Social: ", self.social)
        print("\n")
        print("\n")
        if self.energy == 0 and self.hunger == 0 and self.health == 0:{
            print( "\n X ᴥ Xʔ   R.I.P. \n")
        }


coco = Pou("coco",random.randint(1,3), random.randint(0,10), random.randint(0,10), random.randint(0,10),random.randint(0,10),random.randint(0,10), random.randint(0,10), random.randint(0,10))
print()


while True:
    coco.aging()
    if coco.age >= 10 or coco.hunger <= 0 and coco.health <= 0:
        print(f"\n{coco.name} has died!")
        print( "\n X ᴥ Xʔ   R.I.P. \n\n")
        break


    print("What do you want to do?")
    print("=======================")
    print("     1. Eat")
    print("     2. Sleep")
    print("     3. Play")
    print("     4. Cleaning")
    print("     5. Socialize")
    print("     6. Show status")
    print("     7. Exit")
    print("\n")
    print("\n")
    option = input()
    if option == "1":
        coco.eat()
    elif option == "2":
        coco.sleep()
    elif option == "3":
        coco.play()
    elif option == "4":
        coco.cleaning()
    elif option == "5":
        coco.socialize()
    elif option == "6":
        coco.status()
    elif option == "7":
        break
    else:
        print("What do you want to do?")
        print("\n")
        print("\n")

    time.sleep(1)

    ####
