from amaranth import *

def to_fixed(val):
    return int(val * (2**16))

def from_fixed(val):
    return val / 2**16

def fixed_mult(val1, val2):
    return (val1 * val2) >> 16
