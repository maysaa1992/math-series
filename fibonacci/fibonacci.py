def fibonacci(n):
      if type (n) != int:
        return "please enter a number"
      if n==1 or n==0:
        return n
      else:
        return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(8))