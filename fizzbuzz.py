for x in range (106):
    if(x % 11 == 0) & (x % 13 == 0):
        print("FezzBong")
    elif (x % 3 == 0) & (x % 5 == 0) & (x % 7 == 0) & (x % 13 == 0):
        print("FizzFezzBuzzBang")
    elif (x % 3 == 0) & (x % 7 == 0) & (x % 13 == 0):
        print("FizzFezzBang")
    elif (x % 5 == 0) & (x % 7 == 0) & (x % 13 == 0):
        print("FezzBuzzBang")
    elif (x % 3 == 0) & (x % 5 == 0) & (x % 13 == 0):
        print("FizzFezzBuzz")
    elif(x % 3 == 0) & (x % 13 == 0):
        print("FizzFezz")
    elif(x % 5 == 0) & (x % 13 == 0):
        print("FezzBuzz")
    elif(x % 7 == 0) & (x % 13 == 0):
        print("FezzBang")
    elif(x % 13 == 0):
        print("Fezz")
    elif(x % 11 == 0):
        print("Bong")
    elif (x % 3 == 0) & (x % 5 == 0) & (x % 7 == 0):
        print("FizzBuzzBang")
    elif (x % 3 == 0) & (x % 7 == 0):
        print("FizzBang")
    elif (x % 5 == 0) & (x % 7 == 0):
        print("BuzzBang")
    elif (x % 3 == 0) & (x % 5 == 0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 7 == 0:
        print("Bang")
    else:
        print(x)
