from amaranth import *

def to_fixed(val):
    return int(val * (2**16))

def to_fixed_arr(arr):
    return [to_fixed(val) for val in arr]

def from_fixed(val):
    return val / 2**16

def from_fixed_arr(arr):
    return [val / 2**16 for val in arr]

def fixed_mult(val1, val2):
    return (val1 * val2) >> 16
