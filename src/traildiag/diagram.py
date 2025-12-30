import numpy as np


class TrailDiagram:
    """
    A trail diagram as outlined in the paper.

    Parameters:
    -----------
    markers: int
        number of markers to keep
    interval: int
        at which interval to drop markers
    """

    def __init__(self, markers: int, interval: int):
        self.num_markers = markers
        """how many markers to keep alive"""
        self.interval = interval
        """interval at which to drop markers"""
        self.markers: dict[int, np.ndarray] = {}
        """dictionary of markers, number -> point in X"""
        self.iteration = 0
        """current iteration number - x axis in plots"""
        self.renew = 0
        """time to drop another marker"""
        self.traces: dict[int, list] = {}
        """containst the traces to be plottet"""

    def add_path(self, path: np.ndarray):
        """add the full path to plot"""
        for x in path:
            self.add_step(x, True)

    def add_step(
        self, x: np.ndarray, fx: np.ndarray, dx: np.ndarray, feasibleMarker: bool
    ):
        """
        Add a single step to the trail diagram.

        Parameters:
        -----------
        x: np.ndarray
            point in X
        fx: np.ndarray
            function value at x
        dx: np.ndarray
            gradient at x
        feasibleMarker: bool
            whether to drop a marker at x
        """
        self.iteration += 1
        for j, marker in self.markers.items():
            dist = np.linalg.norm(x - marker)
            trace = self.traces.setdefault(j, [])
            trace.append((self.iteration, float(dist)))
        self.renew -= 1
        if self.renew < 0 and feasibleMarker:
            self.renew = self.interval
            if len(self.markers) >= self.num_markers:
                self.markers.pop(min(self.markers))
            if len(self.markers) == 0:
                self.markers[0] = x
            else:
                mn = max(self.markers) + 1
                self.markers[mn] = x
            pass
        pass
