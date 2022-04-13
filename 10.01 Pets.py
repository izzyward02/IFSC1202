#create a class called Pet w/ following attributes:
#constructor should not have arguments
class Pet():
    def __init__(self, Name, Type, Age):
#   Name = name of pet
#   Type = type of pet (Cat, Dog, etc)
#   Age = age of pet
        self.Name = Name
        self.Type = Type
        self.Age = Age
#Read 10.01 Pets.txt file
petTxt = open("10.01 Pets.txt", "r")
fileRead = petTxt.readline()
petElement = fileRead.split(",")
#   create three pet objects (one per line)
furball1= Pet(petElement[0], petElement[1], petElement[2])
fileRead = petTxt.readline()
petElement = fileRead.split(",")
furball2 = Pet(petElement[0], petElement[1], petElement[2])
fileRead = petTxt.readline()
petElement = fileRead.split(",")
furball3 = Pet(petElement[0], petElement[1], petElement[2])
#   print object attributes for pets using .format() method
print("{:<8}{:<8}{:<8}".format("Name", "Type", "Age"))
#print Name, Type, Age attributes from each pet object
print("{:<8}{:<8}{:<8}".format(furball1.Name, furball1.Type, furball1.Age))
print("{:<8}{:<8}{:<8}".format(furball2.Name, furball2.Type, furball2.Age))
print("{:<8}{:<8}{:<8}".format(furball3.Name, furball3.Type, furball3.Age))
