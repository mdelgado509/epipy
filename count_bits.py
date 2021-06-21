"""Finds the number of set bits in a nonnegative integer"""

def count_bits(x: int) -> int:
    """
    This function counts the number of bits set to 1 in a nonnegative integer

    Runs on O(n) time complexity where `n` is the size of the integer in bits
    """
    # keeps track of num bits
    num_bits = 0
    # while x is truthy
    while x:
        # x bitwise AND 1 results in 1 if the least significant bit is 1
        # or results in 0 if the least significant bit is 0
        # num_bits is incremented by 1 if the least significant bit is set
        num_bits += x & 1
        # x is right shifted by 1 so the program moves on to the second to
        # last least significant bit
        x >>= 1
    # while loop is exited when x is 0 and falsy
    # return num_bits at the end of program
    return num_bits


# Examples
num = 0
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 1
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 2
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 3
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 5
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 8
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
num = 13
print(f"""The binary notation of {num} is {bin(num)}, the bitlength is
    {num.bit_length()}, and the number of set bits is {count_bits(num)}""")
