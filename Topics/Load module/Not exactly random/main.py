# place `import` statement at top of the program
import random

# don't modify this code or variable `n` may not be available
n = int(input())
random.seed(n)
print(random.randint(-100, 100))
# put your code here
