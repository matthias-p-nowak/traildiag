import numpy as np


class Rosenbrock:
    def __init__(self, b: float = 100):
        self.b = b

    def value(self, xy: (float, float)):
        x, y = xy
        return (1.0 - x) ** 2 + self.b * (y - x**2) ** 2

    def gradient(self, xy: (float, float)):
        x, y = xy
        dx = -2 * (1 - x) - 4 * self.b * x * (y - x**2)
        dy = 2 * self.b * (y - x**2)
        return np.array([dx, dy])
