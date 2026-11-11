#Find the Largest Number
a = 25
b = 40
c = 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Numbers:", a, b, c)
print("Largest Number:", largest)