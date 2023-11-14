# Print numbers from 1 to 100
for x in range(1, 101):
  # For multiples of 3, replace x with "Fizz"
  if x % 3 == 0:
    print('Fizz')
  # For multiples of 5, replace x with "Buzz"
  elif x % 5 == 0:
    print('Buzz')
  # For multiples of 3 & 5, replace x with "FizzBuzz"
  elif x % 3 == 0 and x % 5 == 0:
    print('FizzBuzz')
  # For everything else print the value of x
  else:
    print(x)
