a = list(map(int,input().split()))
b = list(map(int,input().split()))

def union(a,b):
    c = []

    for i in a:
        c.append(i)

    for j in b:
        if j not in a:
            c.append(j)

    return c

def intersection(a,b):
    c = []
    for i in b:
        if i in a:
            c.append(i)

    return c

def sub(a,b):
    c = []
    for i in a:

        if i not in b:
            c.append(i)

    return c


def crossintersection(a,b):
    c = union(a,b)
    d = intersection(a,b)
    e = sub(c,d)

    return e


print(union(a,b))
print(intersection(a,b))


print(sub(a,b))
print(crossintersection(a,b))