#Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#Example 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#Example 3
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

#Example 4
newlist = [x for x in range(10)]

#Example 5
newlist = [x for x in range(10) if x < 5]

#Example 6
newlist = [x.upper() for x in fruits]

#Example 7
newlist = ['hello' for x in fruits]

#Example 8
newlist = [x if x != "banana" else "orange" for x in fruits]

