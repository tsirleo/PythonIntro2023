from itertools import product

Struct = type('Struct', (), {'__slots__': []})
[setattr(Struct, seq, seq) for seq in [''.join(chars) for chars in product('abcd', repeat=4)]]


# print(Struct().abba)
