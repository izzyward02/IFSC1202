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
    def InventoryValue(self, UnitsOnHand, Price):
        InventoryValue = self.UnitsOnHand * self.Price
        return InventoryValue
#read 10.02 Inventory.txt file & create three objects, one per item
fileTxt = open("10.02 Inventory.txt", "r")

fileRead = fileTxt.readline()
itemElement = fileRead.split(",")
item1 = RetailItem(itemElement[0], itemElement[1], itemElement[2], InventoryValue)  #CALL LAST PARAMETER SEPARATELY FOR EACH INSTANCE

fileRead = fileTxt.readline()
itemElement = fileRead.split(",")
item2 = RetailItem(itemElement[0], itemElement[1], itemElement[2], InventoryValue)

fileRead = fileTxt.readline()
itemElement = fileRead.split(",")
item3 = RetailItem(itemElement[0], itemElement[1], itemElement[2], InventoryValue)
#display report w/ Description, UnitsOnHand, Price, and InventoryValue
print("{:<8}{:<8}{:<8}{:<8}".format("Description", "Units On Hand", "Price", "Inventory"))

print("{:<8}{:<8}{:<8}{:<8}".format(item1.Description, item1.UnitsOnHand, item1.Price, item1.InventoryValue))
print("{:<8}{:<8}{:<8}{:<8}".format(item2.Description, item2.UnitsOnHand, item2.Price, item2.InventoryValue))
print("{:<8}{:<8}{:<8}{:<8}".format(item3.Description, item3.UnitsOnHand, item3.Price, item3.InventoryValue))

#EXAMPLE OUTPUT:

#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12                9.95              119.40
#      Jeans                  40               34.95             1398.00
#      Shirt                  20               24.95              499.00