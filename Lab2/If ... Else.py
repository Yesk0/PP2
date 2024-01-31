"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
#Example 1
a = 33
b = 200
if b > a:
  print("b is greater than a")
#Example 2
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#Example 3
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#Example 4
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#Example 5
if a > b: print("a is greater than b")
#Example 6
a = 2
b = 330
print("A") if a > b else print("B")
#Example 7
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#Example 8
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#Example 9
  a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#Example 10
  a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#Example 11
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Example 12
a = 33
b = 200

if b > a:
  pass
