def palindrome(x):
    y = x.split()
    y = (' '.join(y[::-1]))
    if x == y:
        print("Palindrome")
    else:
        print("Not Palindrome")
x = input()
palindrome(x)