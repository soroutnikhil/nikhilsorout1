# Ans 1
# a)string
a = "nikhil sorout"
# b) list
b = [1, 1, 2, 5, 5.52, 2, [1, 2], "nikhil"]
# c)flote
c = 21.22
# d) tuple
d = (1, 2, 5, 4, "nikhil")
print(a, b, c, d)

# Ans 2
var1 = 'nikhil'
var2 = '[ds ml python]'
var3 = ['ds', 'ml', 'python']
var4 = 1.0
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

# Ans 3
A = int(input("enter your first number: "))
B = int(input("enter your second number: "))
print(A / B)
print(A % B)
print(A // B)
print(A ** B)

# Ans 4
a = [1, 5, 7, "nikhil" "sorout", 12.2, True, 5, 5, 7, 5]
print(len(a))
for i in a:
    print(i, type(i))

# Ans 5
A = int(input("enter the first number: "))
B = int(input("enter the second number: "))

count = 0

while A % B == 0:
    A = A // B
    count += 1

print(count)

# Ans 6
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for i in a:
    if i % 3 == 0:
        print(f"{i} is divisible by 3")
    else:
        print(f"{i} is not divisible by 3")

# Ans 7
# List are mutable data type and string are immutable data type. When we some chnage on list 
# they are permanent change but we change on string they not change permanant
#  a new object is created with the updated value instead of modifying the original object.

# exapmle

# Mutable data types
a = [1, 2, 3]
a.append(4)
print(a)

# immutable date type
my_string = "Hello"
my_string += " World"
print(my_string)
