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
        return [v1 + v2 for v1,v2 in zip(vector_one, vector_two)]
    else:
        raise ShapeError

def vector_sub(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        return [v1 - v2 for v1,v2 in zip(vector_one, vector_two)]
    else:
        raise ShapeError

def vector_sum(*args):
    vector_shape = [shape(vector) for vector in args]
    if min(vector_shape) == max(vector_shape):
        return [sum(v1) for v1 in zip(*args)]
    else:
        raise ShapeError

def dot(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        return sum([v1 * v2 for v1,v2 in zip(vector_one, vector_two)])
    else:
        raise ShapeError

def vector_multiply(vector, scalar):
    return [(number * scalar) for number in vector]

def vector_mean(*args):
    return [(sum(x)/len(args)) for x in zip(*args)]

def magnitude(vector):
    return ((sum([x**2 for x in vector])))**(1/2)

def matrix_row(matrix, row):
    return matrix[row]

def matrix_col(matrix, col):
    return [row[col] for row in matrix]

def matrix_add(matrix1, matrix2):
    if shape(matrix1) == shape(matrix2):
        return [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    else:
        raise ShapeError

def matrix_matrix_sub(matrix1, matrix2):
    if shape(matrix1) == shape(matrix2):
        return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    else:
        raise ShapeError

def matrix_scalar_multiply(matrix1, scalar):
    result = [[matrix1[i][j]*scalar for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def matrix_vector_multiply(matrix1, vector):
    if len(vector) == len(matrix1[0]):
        return [dot(x, vector) for x in matrix1]
    else:
        raise ShapeError

def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) == len(matrix2):
        return [[sum(a*b for a,b in zip(matrix1_row,matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
    else:
        raise ShapeError
