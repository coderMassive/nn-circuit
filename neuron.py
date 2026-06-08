from amaranth import *
from fixedpoint import fixed_mult

class Neuron(Elaboratable):
    def __init__(self, num_inputs):
        self.inputs = Array([Signal(signed(32)) for _ in range(num_inputs)])
        self.weights = Array([Signal(signed(32)) for _ in range(num_inputs)])
        self.out = Signal(signed(32))

    def elaborate(self, platform):
        m = Module()
        val = 0
        for i in range(len(self.inputs)):
            val += fixed_mult(self.inputs[i], self.weights[i])
        m.d.comb += self.out.eq(val)
        return m
