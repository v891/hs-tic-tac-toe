# put your python code here
a = float(input())
b = float(input())
s = input()

if s == "+":
    print(a + b)
elif s == "-":
    print(a - b)
elif s == "/":
    if b == 0:
        print("Division by 0!")
    else:
        print(a / b)
elif s == "*":
    print(a * b)
elif s == "mod":
    if b == 0:
        print("Division by 0!")
    else:
        print(a % b)
elif s == "pow":
    print(a ** b)
elif s == "div":
    if b == 0:
        print("Division by 0!")
    else:
        print(a // b)
