from vector import Vector
import numpy as np

''' we don't need to change this class , because we changed Vector class to use numpy arrays and in
 this class everything is with vector referencing.  Line--> Vector , Vector-->NumPy , Line-->NumPy 
 We want to use numpy property that use the c++ arrays and increase the speed and we did this.'''


class Line(object):
    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    num_decimal_places = 3

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0] * self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0.0
        self.constant_term = constant_term
        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0] * self.dimension
            initial_index = Line.first_nonzero_index(n.coordinates)
            initial_coefficient = n.coordinates[initial_index]

            basepoint_coords[initial_index] = c / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def write_coefficient(self, coefficient, is_initial_term=False):
        coefficient = round(coefficient, self.num_decimal_places)

        if coefficient % 1 == 0:
            coefficient = int(coefficient)
        output = ''

        if coefficient < 0:
            output += '-'
        if coefficient > 0 and not is_initial_term:
            output += '+'
        if not is_initial_term:
            output += ' '
        if abs(coefficient) != 1:
            output += '{}'.format(abs(coefficient))

        return output

    def __str__(self):
        n = self.normal_vector
        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [self.write_coefficient(n[i], is_initial_term=(i == initial_index)) +
                     'x_{}'.format(i + 1) for i in range(self.dimension) if round(n[i],
                      self.num_decimal_places) != 0]
            output = ' '.join(terms)
        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, self.num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)
        return output

    @staticmethod
    def first_nonzero_index(iterable):
        eps = 1e-10
        for k, item in enumerate(iterable):
            if not abs(item) < eps:
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel(self, v):
        ratio = self.normal_vector.coordinates[0] / v.normal_vector.coordinates[0]
        i = 1
        while i < self.dimension :
            if self.normal_vector.coordinates[i] / v.normal_vector.coordinates[i] != ratio:
                return False
            i += 1
        return True

    def is_equal(self, v):
        p0 = self.basepoint
        p1 = v.basepoint
        i = p1.coordinates[0]-p0.coordinates[0]
        j = p1.coordinates[1]-p0.coordinates[1]
        A = Vector([i, j])
        if A.is_parallel(self.normal_vector) and A.is_parallel(v.normal_vector):
            return True
        return False

    def get_intersect(self, v):
        if self.is_parallel(v):
            raise ValueError

        A = self.normal_vector.coordinates[0]
        B = self.normal_vector.coordinates[1]
        C = v.normal_vector.coordinates[0]
        D = v.normal_vector.coordinates[1]
        k1 = self.constant_term
        k2 = v.constant_term

        try:
            x = (D*k1 - B*k2) / (A*D-B*C)
            y = ((-1*C*k1) + (A*k2)) / (A*D-B*C)
            if x == 0 and y == 0 :
                return 'same line'
            return [x, y]
        except ZeroDivisionError:
            print('No Intersection')
