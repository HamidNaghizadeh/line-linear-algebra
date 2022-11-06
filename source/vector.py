import numpy as np


class Vector:
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = np.array(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __add__(self, v):
        return self.coordinates + v.coordinates

    def __sub__(self, v):
        return self.coordinates - v.coordinates

    def scalar_multiplication(self, a):
        return self.coordinates * a

    def is_parallel(self, v):
        ratio = self.coordinates[0] / v.coordinates[0]
        i = 1
        while i < self.dimension:
            if self.coordinates[i] / v.coordinates[i] != ratio:
                return False
            i += 1
        return True
