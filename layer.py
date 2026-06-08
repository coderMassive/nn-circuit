from amaranth import *
from neuron import Neuron

class Layer(Elaboratable):
    def __init__(self, num_inputs, num_neurons, activation):
        self.inputs = Array([Signal(signed(32)) for _ in range(num_inputs)])
        self.neurons = [Neuron(num_inputs) for _ in range(num_neurons)]
        self.activation = activation
        self.out = Array([Signal(signed(32)) for _ in range(num_neurons)])

    def elaborate(self, platform):
        m = Module()
        for i, neuron in enumerate(self.neurons):
            m.submodules[f"neuron_{i}"] = neuron
            for j in range(len(self.inputs)):
                m.d.comb += neuron.inputs[j].eq(self.inputs[j])
            m.d.comb += self.out[i].eq(self.activation(neuron.out))
        return m
