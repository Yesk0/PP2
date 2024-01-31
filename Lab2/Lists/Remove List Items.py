#Example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Example 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#Example 3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Example 4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Example 5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Example 6
thislist = ["apple", "banana", "cherry"]
del thislist
#Example 7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
