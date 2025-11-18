#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    al = len(tuple_a)
    bl = len(tuple_b)
    ll = 0
    new = []
    if al > bl:
        for i in range(al):
            if i < bl:
                new.append(tuple_a[i]+tuple_b[i])
            else:
                new.append(tuple_a[i])

    else:
        for i in range(bl):
            if i < al:
                new.append(tuple_a[i]+tuple_b[i])
            else:
                new.append(tuple_b[i])
    return tuple(new)
