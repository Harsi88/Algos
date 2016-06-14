import random as r


def generate(n,l,a):
    """
    Generates random list a of length n having elements in range -l to l
    """
    for i in range(0,n):
        a.append(r.randrange(-l,l))

