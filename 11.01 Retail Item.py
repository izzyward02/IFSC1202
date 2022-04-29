#create class RetailItem 
class RetailItem():
#   class should have the following attributes:
#       Description default ("")
#       UnitsOnHand default (0)
#       Price default (0)
    def __init__(self, Description = "", UnitsOnHand = 0, Price = 0):
#   create constructor of RetailItem that accepts Description, UnitsOnHand, and Price then sets then to attributes in class
#       if one item is not present, set attribute to default value
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
#   create method InventoryValue that returns UnitsOnHand * Price
    def InventoryValue(self):
        InventoryValue = self.UnitsOnHand * self.Price
        InventoryValue = round(InventoryValue, 2)
        return InventoryValue
#   create print_inventory w/ list as the argument (prints list w/ headings)
def print_inventory(lists):
    print("{:>15}{:>15}{:^15}{:>15}".format("Description", "Units On Hand", "Price", "Inventory Value"))
    for a in range(len(lists)):
        print("{:>15}{:>15}{:^15}{:>15}".format(lists[a].Description, str(lists[a].UnitsOnHand), str(lists[a].Price), lists[a].InventoryValue()))
#   print list of items w/ initial inventory value using RetailItem attributes
    print()
#   create find_inventory w/ list & name of inventory item as arguments (searches list for a match & returns)
def find_inventory(lists, listItem):
    for a in range(len(lists)):
        if lists[a].Description == listItem:
            return a
    return -1
#   read 11.01 Inventory.txt & create list of items
fileTxtA = open("11.01 Inventory.txt", "r")
fileRead = fileTxtA.readline()
itemList = []
while fileRead != "":
    itemData = fileRead.split(",")
    item1 = RetailItem(itemData[0].strip(), float(itemData[1].strip()), float(itemData[2].strip()))
    itemList.append(item1)
    fileRead = fileTxtA.readline()
fileTxtA.close()
print_inventory(itemList)
#   read 11.01 InventoryUpdate.txt, search for an item to update & update Price
fileTxtB = open("11.01 InventoryUpdate.txt", "r")
fileRead = fileTxtB.readline()
itemUpdate = []
while fileRead != "":
    itemData = fileRead.split(",")
    itemList[find_inventory(itemList, itemData[0])].Price = float(itemData[2])
    fileRead = fileTxtB.readline()
fileTxtB.close()
print_inventory(itemList)
print()
