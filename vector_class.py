import math
from nose.tools import raises

class ShapeError(Exception):
    pass

class VectorMath:
    def __init__(self):
        pass

    def shape(self, vector_matrix):
        rows = len(vector_matrix)
        if type(vector_matrix[0]) == type([]):
            columns = len(vector_matrix[0])
            return (rows, columns)
        else:
            return (rows, )

    def compare_shapes(self, *args):
        if len(set([shape(arg) for arg in args])) == 1:
            return shape

    def vector_add(self, vector_one, vector_two):
        if shape(vector_one) == shape(vector_two):
            return [v1 + v2 for v1,v2 in zip(vector_one, vector_two)]
        else:
            raise ShapeError

    def vector_sub(self, vector_one, vector_two):
        if shape(vector_one) == shape(vector_two):
            return [v1 - v2 for v1,v2 in zip(vector_one, vector_two)]
        else:
            raise ShapeError

    def vector_sum(self, *args):
        vector_shape = [shape(vector) for vector in args]
        if min(vector_shape) == max(vector_shape):
            return [sum(v1) for v1 in zip(*args)]
        else:
            raise ShapeError

    def dot(self, vector_one, vector_two):
        if shape(self.vector_one) == shape(self.vector_two):
            return sum([v1 * v2 for v1,v2 in zip(self.vector_one, self.vector_two)])
        else:
            raise ShapeError

    def vector_multiply(self, vector, scalar):
        return [(number * self.scalar) for number in vector]

    def vector_mean(self, *args):
        return [(sum(x)/len(args)) for x in zip(*args)]

    def magnitude(self, vector):
        return ((sum([x**2 for x in vector])))**(1/2)

    def matrix_row(self, matrix, row):
        return matrix[row]

    def matrix_col(self, matrix, col):
        return [row[col] for row in matrix]

    #def matrix_add(matrix_1, matrix_2)
