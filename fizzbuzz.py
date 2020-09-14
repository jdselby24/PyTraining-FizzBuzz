for x in range(101):
    output = ""
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
    if(output == ""):
        print(x)
    print(output)
