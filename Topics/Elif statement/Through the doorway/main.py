a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())

if a > x and b > x and c > x:
    print("The box cannot be carried")
elif a > y and b > y and c > y:
    print("The box cannot be carried")
else:
    print("The box can be carried")
