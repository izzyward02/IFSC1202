#create class called RetailItem that holds data about item in store
class RetailItem():
#class should have following attributes:
#   Description: description of item (default = "")
#   UnitsOnHand: num units in inventory (default = 0)
#   Price: item's retail price (default = 0)
    def __init__(self, Description = "", UnitsOnHand = 0, Price = 0):
#create constructor that accepts Description, UnitsOnHand, and Price & sets to attributes in RetailItem class
#   if one attribute is not present, set attribute to default value
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
#create method InventoryValue that returns UnitsOnHand times Price
    def InventoryValue(self):
        InventoryValue = self.UnitsOnHand * self.Price
        InventoryValue = round(InventoryValue, 2)
        return InventoryValue
#read 10.02 Inventory.txt file & create three objects, one per item
fileTxt = open("10.02 Inventory.txt", "r")
itemList = []
fileRead = fileTxt.readline()

while fileRead != "":
    Description, UnitsOnHand, Price = fileRead.split(",")
    itemData = RetailItem(str(Description), int(UnitsOnHand), float(Price))
    itemList.append(itemData)
    fileRead = fileTxt.readline()

print("{:<20}{:<20}{:<20}{:<20}".format("Description", "Units On Hand", "Price", "Inventory Value"))
#display report w/ Description, UnitsOnHand, Price, and InventoryValue
for i in range(len(itemList)):
    print("{:<20}{:<20}{:<20}{:<20}".format(itemList[i].Description, itemList[i].UnitsOnHand, itemList[i].Price, itemList[i].InventoryValue()))
print()
