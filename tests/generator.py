import rosebrock

import numpy as np


def generate_rosenbrock(n: int):
    """Generates a sequence of values from Rosenbrock function"""
    rb = rosebrock.Rosenbrock()
    x0 = np.array([-1.0, 2.0])
    lr = 0.001
    x = x0
    for i in range(n):
        fx = rb.value(x)
        dx = rb.gradient(x)
        yield (x, fx, dx)
        x = x.copy() - lr * dx
