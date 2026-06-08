from amaranth import *
from amaranth.sim import Simulator
from fixedpoint import *
from neuron import Neuron
from layer import Layer

# Neuron Test

def test_neuron():
    dut = Neuron(2)
    sim = Simulator(dut)

    async def bench_neuron(ctx):
        tests = [[[1, 1], [1, 2]],
                 [[1, -1], [-1, 2]],
                 [[1, -1], [1, -2]],
                 [[1, -1], [2, 0.5]],
                 [[1, 2], [0, 0]]]

        for test in tests:
            for j in range(2):
                ctx.set(dut.inputs[j], to_fixed(test[0][j]))
                ctx.set(dut.weights[j], to_fixed(test[1][j]))

            expected_val = 0
            for k in range(2):
                expected_val += test[0][k] * test[1][k]

            actual_val = from_fixed(ctx.get(dut.out))
            assert actual_val == expected_val

    sim.add_testbench(bench_neuron)
    sim.run()

# Layer Test

def test_layer():
    dut = Layer(num_inputs=2, num_neurons=2, activation=lambda x: x)
    sim = Simulator(dut)

    async def bench_layer(ctx):
        inputs = [-2, 0.5]
        weights = [[1, 1], [-0.5, 3]]

        for i in range(2):
            for j in range(2):
                ctx.set(dut.neurons[i].weights[j], to_fixed(weights[i][j]))

        for k in range(2):
            ctx.set(dut.inputs[k], to_fixed(inputs[k]))

        for l in range(2):
            expected_val = 0
            for m in range(2):
                expected_val += weights[l][m] * inputs[m]
            
            actual_val = from_fixed(ctx.get(dut.out[l]))
            assert actual_val == expected_val

    sim.add_testbench(bench_layer)
    sim.run()
