#txt file w/ stock prices for a week, one per line

#program should perform the following:
#   open & read first line of 06.02 Stock.txt
fileTxt = open("06.02 Stock.txt")
tStock = fileTxt.readline()
print("{0:>10s} {1:>10s}".format("Price", "Change"))
yStock = 0
#   define function "percentChange"
#       accept today's stock price (float) & yesterday's stock price (float) as parameters
#       calculate percent change between yesterday's & today's stock price
#           % change = ((today's value - yesterday's value) / yesterday's value) * 100
def percentChange(tStock, yStock):
    pChange = ((tStock - yStock) / yStock) * 100
    return pChange
#   print headings & first stock value (b/c no percent change on first day)
while tStock != " ":
    tStock = float(tStock)
    if yStock == 0:
        print("{:10.2f}".format(tStock))
        yStock = tStock
        tStock = fileTxt.readline()
    else:
        pChange = (percentChange(tStock,yStock))
        yStock = tStock
        print("{:10.2f} {:10.2f}%".format(tStock, pChange))
        tStock = fileTxt.readline()
#   read next line of input
#   calculate & print stock value & percent change from yesterday 
#       each column is 10 characters wide w/ space between
