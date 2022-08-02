import random
import csv
import os


class JunkFood:
    def __init__(self, name, price, provider, pronoun, ingredient):
        self.name = name    
        self.price = price
        self.inDollars = "${:,.2f}".format(price)
        self.provider = provider
        self.pronoun = pronoun
        self.ingredient = ingredient
    
    def __lt__(self, other):
         return self.price < other.price

    def printItem(self):
        print("Have", self.pronoun, self.name, ", which costs", self.inDollars, " from ", self.provider)


def writeFaveToFile(fave):
    with open('faves.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([fave.name, fave.price, fave.provider, fave.pronoun, fave.ingredient])

def makeListofFavesFromFile():
    faves = []
    with open('faves.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            faves.append(JunkFood(row[0], float(row[1]), row[2], row[3], row[4]))
    return faves

def addFave(faves):
    name = input("What's the name of the food? ")
    price = float(input("How much does it cost? "))
    provider = input("Who makes it? ")
    pronoun = input("What's the pronoun? ")
    ingredient = input("What's the main ingredient? ")
    newFave = JunkFood(name, price, provider, pronoun, ingredient)
    writeFaveToFile(newFave)
    faves.append(newFave)
    print("\n", newFave.name, "was added to your list.")

def removeFave(faves):
    listFaves(faves)
    name = input("What's the name of the fave you want to remove? ")
    with open('faves.csv', 'r') as inp, open('faves_edit.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != name:
                writer.writerow(row)
        os.remove('faves.csv')
        os.rename('faves_edit.csv', 'faves.csv')

def chooseRandom(arr):
    choice = faves[random.randrange(len(arr))]
    choice.printItem()

def listFaves(faves):
    print("\nHere's a list of your favorites:")
    for fave in faves:
        print("-", fave.name, 'from', fave.provider)

def listFavesByPriceAscending(faves):
     sortedFaves = sorted(faves, key=lambda x: x.price)
     for fave in sortedFaves:
         print("-", fave.name + ": " + fave.inDollars)

def userInterface(faves):
    print("\nTime for some junk food!")
    running = True
    listOptions = "\nEnter a number to select an option from the list.\n 1) Pick a random treat.\n 2) Print a list of your faves.\n 3) Print a list of your faves starting with cheapest.\n 4) Add a favorite to your list.\n 5) Remove a favorite to your list.\n Q) Quit Program.\n"
    while(running):
        userChoice = input(listOptions)
        if userChoice == "1":
            chooseRandom(faves)
        elif userChoice == "2":
            listFaves(faves)
        elif userChoice == "3":
            listFavesByPriceAscending(faves)
        elif userChoice == "4":
            addFave(faves)
        elif userChoice == "5":
            removeFave(faves)
            faves = []
            makeListofFavesFromFile()
        elif userChoice == 'Q' or userChoice == "q":
            print("\nHappy Eating!\n")
            running = False
        else:
            print("\nSorry. That choice isn't on the menu.")
              
print("Loading faves...")
faves = makeListofFavesFromFile()
userInterface(faves)

#things to add
# list foods by category
# format out put to look nicer
