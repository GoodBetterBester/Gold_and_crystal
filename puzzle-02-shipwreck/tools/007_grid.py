"""ELDORIA-007: fill the 4 x 7 grid and read the wreck's name.

Tries every order of the four names; only north, east, south, west gives a word.
"""
import itertools

NUMS = [(27, 0), (17, 0), (20, 4), (8, 0), (23, 0), (6, 0), (19, -3), (11, 5), (15, 0), (25, -7)]
NAMES = ["BIMINI", "MAYAGUANA", "BAJONUEVO", "ZAMA"]

def decode(grid):
    return "".join(chr((ord(grid[n - 1]) - 65 + k) % 26 + 65) for n, k in NUMS)

if __name__ == "__main__":
    for perm in itertools.permutations(NAMES):
        print(" ".join(perm), "->", decode("".join(perm)))
