# Print numbers from 1 to 100
for x in range(1, 100 + 1):
    # For multiples of 3, print "Fizz" instead of the number
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    # For multiples of 5, print "Buzz" instead of the number
    elif x % 3 == 0:
        print("Fizz")
    # For multiples of 3 and 5, print "FizzBuzz"
    elif x % 5 == 0:
        print("Buzz")
    # For all other numbers print the numbers only
    else:
        print(x)