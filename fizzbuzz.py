import sys
import re

# To make command line arguments work, include the rules you dont want to run after the file name
# e.g py ./fizzbuzz.py 5 7     this would exclude rules for 3 and 7

maxNum = int(input("Please enter a maximum number:"))

for x in range(maxNum):
    output = ""
    storeArray = []
    if(x % 11 == 0) & ('11' not in sys.argv):
        print("Bong")
        continue
    if(x % 3 == 0) & ('3' not in sys.argv):
        output += "Fizz"
    if(x % 13 == 0) & ('13' not in sys.argv):
        output += "Fezz" 
    if(x % 5 == 0) & ('5' not in sys.argv):
        output += "Buzz"
    if(x % 7 == 0) & ('7' not in sys.argv):
        output += "Bang"
    if(x % 17 == 0) & ('17' not in sys.argv):
        storeArray = re.findall('[A-Z][^A-Z]*', output)
        storeArray.reverse()
        output = ''.join(storeArray)
    if(output == ""):
        print(x)
    else:
        print(output)
