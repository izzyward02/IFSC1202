#txt file w/ stock prices for a week, one per line

#program should perform the following:
#   open & read first line of 06.02 Stock.txt
fileTxt = open("06.02 Stock.txt")
rLine = fileTxt.readline()
#   define function "percentChange"
#       accept today's stock price (float) & yesterday's stock price (float) as parameters
#       calculate percent change between yesterday's & today's stock price
#           % change = ((today's value - yesterday's value) / yesterday's value) * 100
def percentChange(tStock, yStock):
    pChange = ((tStock - yStock) / yStock) * 100
    return pChange
#   print headings & first stock value (b/c no percent change on first day)

#   read next line of input
#   calculate & print stock value & percent change from yesterday 
#       each column is 10 characters wide w/ space between

#EXPECTED OUTPUT:

#     Price      Change
#    126.18
#    125.60      -0.46%
#    125.01      -0.47%
#    127.74       2.18%
#    129.04       1.02%