from amaranth import *

class ReLU(Elaboratable):
    def __init__(self, num_inputs):
        self.inputs = Array([Signal(signed(32)) for _ in range(num_inputs)])
        self.outputs = Array([Signal(signed(32)) for _ in range(num_inputs)])

    def elaborate(self, platform):
        m = Module()
        for i in range(len(self.inputs)):
            with m.If(self.inputs[i] > 0):
                m.d.comb += self.outputs[i].eq(self.inputs[i])
            with m.Else():
                m.d.comb += self.outputs[i].eq(0)
        return m
