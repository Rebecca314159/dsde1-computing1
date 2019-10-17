from math import pi as pi

def period(L,g):
    if type(L) != int and type(L) != float:
        raise TypeError
    if type(g) != int and type(L) != float:
        raise TypeError
    if g == 0:
        raise ValueError
    if g < 0 and L > 0:
        raise ValueError
    if g >0 and L<0:
        raise ValueError
    first = (float(L)/float(g))**0.5
    T = first*2*pi
    return T


