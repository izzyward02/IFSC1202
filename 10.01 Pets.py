#create a class called Pet w/ following attributes:
#constructor should not have arguments
class Pet():
#   Name = name of pet
#   Type = type of pet (Cat, Dog, etc)
#   Age = age of pet
    def __init__(self, name, species, age):
#Read 10.01 Pets.txt file
        petTxt = open("10.01 Pets.txt", "r")
        petRead = petTxt.readline()
        petList = []
#   create three pet objects (one per line)
        self.petName = name
        self.petType = species
        self.petAge = age
#   print object attributes for pets using .format() method
print("   Name     Type     Age")
while petRead != "":
    split = petRead.split(" ")
    petList.append(split)
    petRead = petTxt.readline()

for a in range(len(petList)):
    furballName = Pet(petList[a])
    for b in range(len(petList[a])):
        furballType = Pet(petList[0][b])
        for c in range(len(petList[a][b][c])):
            furballAge = Pet(petList[0][0][c])
furball = Pet(petList[a][b][c])
#print Name, Type, Age attributes from each pet object
print("     {}     {}     {}".format(furball.petName, furball.petType, furball.petAge))
#EXAMPLE OUTPUT:

#   Name    Type     Age
#    Fido     Dog       3
#  Fluffy     Cat       5
#  Tweety    Bird       4