import math
import random

############################
## Wiener's Attack module ##
############################

# Calculates bitlength


def bitlength(x):
    assert x >= 0
    n = 0
    while x > 0:
        n = n + 1
        x = x >> 1
    return n

# Squareroots an integer


def isqrt(n):
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y

# Checks if an integer has a perfect square


def is_perfect_square(n):
    h = n & 0xF  # last hexadecimal "digit"
    if h > 9:
        return -1  # return immediately in 6 cases out of 16.
    # Take advantage of Boolean short-circuit evaluation
    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        # take square root if you must
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1
    return -1

# Calculate a sequence of continued fractions


def partial_quotiens(x, y):
    partials = []
    while x != 1:
        partials.append(x // y)
        a = y
        b = x % y
        x = a
        y = b
    # print partials
    return partials

# Helper function for convergents


def indexed_convergent(sequence):
    i = len(sequence) - 1
    num = sequence[i]
    denom = 1
    while i > 0:
        i -= 1
        a = (sequence[i] * num) + denom
        b = num
        num = a
        denom = b
    #print (num, denom)
    return (num, denom)

# Calculate convergents of a  sequence of continued fractions


def convergents(sequence):
    c = []
    for i in range(1, len(sequence)):
        c.append(indexed_convergent(sequence[0:i]))
    # print c
    return c

# Calculate `phi(N)` from `e`, `d` and `k`


def phiN(e, d, k):
    return ((e * d) - 1) / k

# Wiener's attack, see http://en.wikipedia.org/wiki/Wiener%27s_attack for
# more information


def wiener_attack(N, e):
    (p, q, d) = (0, 0, 0)
    conv = convergents(partial_quotiens(e, N))
    for frac in conv:
        (k, d) = frac
        if k == 0:
            continue
        y = -(N - phiN(e, d, k) + 1)
        discr = y * y - 4 * N
        if(discr >= 0):
            # since we need an integer for our roots we need a perfect squared
            # discriminant
            sqr_discr = is_perfect_square(discr)
            # test if discr is positive and the roots are integers
            if sqr_discr != -1 and (-y + sqr_discr) % 2 == 0:
                p = ((-y + sqr_discr) / 2)
                q = ((-y - sqr_discr) / 2)
                return p, q, d
    return p, q, d
e = 65219466066769322959685729260329028844219822281959711995309237814578885589834164958374105487943403650470073482735700046123974989274174297404847386235498586071113443380305491163903141856357651771596007202719976790919126923577469583256818014041312957797087344618937694004308786671770946160273290589624526161439
n = 73636387548687441806927850345791294638237440748805326286524943553228804832086420507567421324949631001899025807735987635229148699907990293227474341203714197760116769619744250003618455212002668366122234785381531988050730998684466621988368695831629757292957761871604035934446625044473743809458555600023616396927
c = 24307286749984085952207174076446513214101479971796813984732804608019085127244978501519304964860570113410818778814923004062482229566704856031258548156367606911445377341191871278149146796476671973589754837443608646041830738863019602218954296730454212999657751175008263103922023152796223448297921222983990470443
p, q, d = wiener_attack(n, e)

print(hex(pow(c,d,n))[2:-1].decode('hex'))

################################
## End Wiener's Attack module ##
################################
