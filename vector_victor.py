import math
from nose.tools import raises

class ShapeError(Exception):
    pass

def shape(vector_matrix):
    rows = len(vector_matrix)
    if type(vector_matrix[0]) == type([]):
        columns = len(vector_matrix[0])
        return (rows, columns)
    else:
        return (rows, )

def compare_shapes(*args):
    if len(set([shape(arg) for arg in args])) == 1:
        return shape

def vector_add(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        add_vectors = [v1 + v2 for v1,v2 in zip(vector_one, vector_two)]
        return add_vectors
    else:
        raise ShapeError

def vector_sub(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        sub_vectors = [v1 - v2 for v1,v2 in zip(vector_one, vector_two)]
        return sub_vectors
    else:
        raise ShapeError

def vector_sum(*args):
    vector_shape = [shape(vector) for vector in args]
    if min(vector_shape) == max(vector_shape):
        vectors_summed = [sum(v1) for v1 in zip(*args)]
        return vectors_summed
    else:
        raise ShapeError

def dot(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        dot_vectors = sum([v1 * v2 for v1,v2 in zip(vector_one, vector_two)])
        return dot_vectors
    else:
        raise ShapeError

def vector_multiply(vector, scalar):
    return [(number * scalar) for number in vector]

def mean(*args):
    return sum(*args)/len(*args)

def vector_mean(*args):
    return [(sum(x)/len(args)) for x in zip(*args)]

def magnitude(vector):
    return ((sum([x**2 for x in vector])))**(1/2)
