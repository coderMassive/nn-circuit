from amaranth import *
from amaranth.sim import Simulator
from fixedpoint import *

# Neuron

from neuron import Neuron
dut = Neuron(2)

async def bench_neuron(ctx):
    tests = [[[1, 1], [1, 2]],
             [[1, -1], [-1, 2]],
             [[1, -1], [1, -2]],
             [[1, -1], [2, 0.5]],
             [[1, 2], [0, 0]]]

    for (i, test) in enumerate(tests):
        for j in range(2):
            ctx.set(dut.inputs[j], to_fixed(test[0][j]))
            ctx.set(dut.weights[j], to_fixed(test[1][j]))

        val = 0
        for k in range(2):
            val += test[0][k] * test[1][k]

        assert from_fixed(ctx.get(dut.out)) == val

def test_neuron():
    sim = Simulator(dut)
    sim.add_testbench(bench_neuron)
    sim.run()
