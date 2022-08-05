from nis import cat
import random
import csv
import os


class JunkFood:
    def __init__(self, name, price, provider, pronoun, category):
        self.name = name    
        self.price = price
        self.inDollars = "${:,.2f}".format(price)
        self.provider = provider
        self.pronoun = pronoun
        self.category = category
    
    def __lt__(self, other):
         return self.price < other.price

    def printItem(self):
        print('\033[1m' + f"Have {self.pronoun} {self.name}. That costs {self.inDollars}. Get it from {self.provider}." + '\033[0m')


def writeFaveToFile(fave):
    with open('faves.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([fave.name, fave.price, fave.provider, fave.pronoun, fave.category])

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
    category = input("What category would you group this in? ")
    newFave = JunkFood(name, price, provider, pronoun, category)
    writeFaveToFile(newFave)
    faves.append(newFave)
    print("\n", newFave.name, "was added to your list.")

def removeFave(faves):
    listFaves(faves)
    name = input("\nWhat's the name of the fave you want to remove? ")
    with open('faves.csv', 'r') as inp, open('faves_edit.csv', 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            if row[0] != name:
                writer.writerow(row)
            else:
                print(f"Removing {name}.")
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
         print(f"- {fave.name:<25} {fave.inDollars: >{6}}")

def pickAFaveByCategory(faves):
    categories = sorted(list({fave.category for fave in faves}))
    print("\nHere's a list of categories to choose from:")
    for index, category in enumerate(categories):
        print(f"{index + 1}) {category}")
    choice = int(input("Choose a category by number."))
    if isinstance(choice, int)  and choice in range(1, len(categories)+1):
        print("\nTry one of these...")
        for fave in faves:
            if fave.category == categories[choice - 1]:
                fave.printItem()
    else:
        print("That's not an option.")

def userInterface(faves):
    print("\nTime for some junk food!")
    running = True
    optionsList = """
Enter a number to select an option from the list.
1) Pick a random treat.
2) Print a list of your faves.
3) Print a list of your faves starting with cheapest.
4) Pick a treat from a chosen category.
5) Add a favorite to your list.
6) Remove a favorite from your list.
Q) Quit Program.

"""
    
    while(running):
        userChoice = input(optionsList)
        if userChoice == "1":
            chooseRandom(faves)
        elif userChoice == "2":
            listFaves(faves)
        elif userChoice == "3":
            listFavesByPriceAscending(faves)
        elif userChoice == "4":
            pickAFaveByCategory(faves)
        elif userChoice == "5":
            addFave(faves)
        elif userChoice == "6":
            removeFave(faves)
            faves = makeListofFavesFromFile()
        elif userChoice == 'Q' or userChoice == "q":
            print("\nHappy Eating!\n")
            running = False
        else:
            print("\nSorry. That choice isn't on the menu.")
              
print("\nLoading faves...")
faves = makeListofFavesFromFile()
userInterface(faves)

#things to add
# handle bad input
# format output to look nicer
