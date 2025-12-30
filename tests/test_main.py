from traildiag.diagram import TrailDiagram

from generator import generate_rosenbrock


def test_main():
    diag = TrailDiagram(3, 5)
    for x, fx, dx in generate_rosenbrock(20):
        diag.add_step(x, fx, dx, True)


if __name__ == "__main__":
    test_main()
