#create class RetailItem 
#   class should have the following attributes:
#       Description default ("")
#       UnitsOnHand default (0)
#       Price default (0)
#   create constructor of RetailItem that accepts Description, UnitsOnHand, and Price then sets then to attributes in class
#       if one item is not present, set attribute to default value
#   create method InventoryValue that returns UnitsOnHand * Price
#   read 11.01 Inventory.txt & create list of items
#   print list of items w/ initial inventory value using RetailItem attributes
#   read 11.01 InventoryUpdate.txt, search for an item to update & update Price
#   print list w/ updated values
#   create print_inventory w/ list as the argument (prints list w/ headings)
#   create find_inventory w/ list & name of inventory item as arguments (searches list for a match & returns)

#EXPECTED OUTPUT:

#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12                9.95              119.40
#      Jeans                  40               34.95             1398.00
#      Shirt                  20               24.95              499.00

#Description       Units On Hand               Price     Inventory Value
#     Jacket                  12               10.95              131.40
#      Jeans                  40               35.95             1438.00
#      Shirt                  20               25.95              519.00