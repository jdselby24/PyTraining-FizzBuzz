for x in range (0, 101):
    print(x)
    if (x % 3 == 0) & (x % 5 ==0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")