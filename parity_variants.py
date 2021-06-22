"""
Write expressions that use bitwise operators, equality checks, Booklean
operators to do the following in O(1) time
"""

def is_power_two(x: int) -> bool:
    """
    Test if x is a power of 2
    Evaluates true for x = 1, 2, 4, 8, ..., false for all other values

    x != 0 handles the edge case where x = 0
    x & (x - 1) evaluates to 0 & -1 which evaluates to 0
    0 is not a power of two so the conditional `and` makes sure
    to return false if the value of x is 0
    """
    return x & (x - 1) == 0 and x != 0

print(is_power_two(0))
print(is_power_two(1))
print(is_power_two(2))
print(is_power_two(3))
print(is_power_two(4))
print(is_power_two(5))
print(is_power_two(6))
print(is_power_two(7))
print(is_power_two(8))
print(is_power_two(9))
print(is_power_two(10))
def mod_power_two(x, p: int) -> int:
    """
    Compute x mod a power of two
    e.g. returns 13 for 77 mod 64 (2 ** 6)
    """
    return x & ((1 << p) - 1)

print(mod_power_two(77, 6) == 77 % (2 ** 6))
print(mod_power_two(77, 5) == 77 % (2 ** 5))
print(mod_power_two(77, 4) == 77 % (2 ** 4))
print(mod_power_two(77, 3) == 77 % (2 ** 3))
print(mod_power_two(77, 2) == 77 % (2 ** 2))
print(mod_power_two(77, 1) == 77 % (2 ** 1))

def right_propagate_rightmost_set_bit(x: int) -> int:
    """
    Right propagate the rightmost set bit in x
    e.g. turns 0b01010000 to 0b01011111
    """
    return x | (x - 1)

print(right_propagate_rightmost_set_bit(0b1010000) == 0b01011111)
