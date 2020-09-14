import re

for x in range(500):
    output = ""
    storeArray = []
    if(x % 11 == 0):
        print("Bong")
        continue
    if(x % 3 == 0):
        output += "Fizz"
    if(x % 13 == 0):
        output += "Fezz" 
    if(x % 5 == 0):
        output += "Buzz"
    if(x % 7 == 0):
        output += "Bang"
    if(x % 17 == 0):
        storeArray = re.findall('[A-Z][^A-Z]*', output)
        storeArray.reverse()
        output = ''.join(storeArray)
    if(output == ""):
        print(x)
    else:
        print(output)
