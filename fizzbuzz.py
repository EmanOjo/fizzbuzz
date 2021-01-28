

def multiple_3_fizz(n):
  return n % 3 == 0

def multiple_5_fizz(n):
  return n % 5 == 0

def multiple_15_fizz(n):
  return n % 15 == 0

def to_fizzbuzz(n):
  return 'FizzBuzz' if multiple_15_fizz(n) else 'Fizz' if multiple_3_fizz(n) else 'Buzz' if multiple_5_fizz(n) else n



def fizzbuzz(n):
    list = []
    for i in range(1, n+1):
        list.append(to_fizzbuzz(i))
    return list
