def uniqset(x):
    unqs = []
    for i in x:
        if i not in unqs:
            unqs.append(i)
    print(unqs)

x = [1, 2, 2, 5, 6, 1, 3, 6]
uniqset(x)


