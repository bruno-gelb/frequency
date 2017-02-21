#!/usr/bin/env python
# coding: utf-8

import numpy as np

DATA = np.genfromtxt("data.txt", dtype=int)
SIZE = 4


def count_occurrences (data, pattern):
    '''Find all occurrences of pattern and count them'''
    pattern = np.fromstring (pattern, dtype=int, sep=' ')
    pattern_len = np.shape(pattern)[0]
    data_len = np.shape(data)[0] # data[data_len] is not already allowed to call
    occurrences_amount = 0
    index = 0
    for value in data:
        if value == pattern[0]: # possible start of pattern
            start = index
            if start + pattern_len >= data_len: # if pattern doesn't fit into sequence
                break
            else: # check is it pattern
                is_match = True
                for p in xrange(pattern_len):
                    if data[start + p] != pattern[p]: # it is not
                        is_match = False
                        break
                if is_match:
                    occurrences_amount += 1
        index += 1
    return occurrences_amount


def gen_2d_frequency_matrix(data, size):
    '''Generates 2d frequency matrix'''    
    frequency_matrix = np.empty((size, size))
    for i in xrange(size):
        for j in xrange(size):
            pattern = ' '.join(str(x) for x in [i + 1, j + 1])
            frequency_matrix[i, j] = count_occurrences(data, pattern)
    return frequency_matrix


def gen_3d_frequency_matrix(data, size):
    '''Generates 3d frequency matrix'''    
    frequency_matrix = np.zeros((size ** 2, size))
    import itertools
    patterns = []
    for i, j, k in itertools.product(xrange(size), xrange(size), xrange(size)):
        patterns.append(' '.join(str(i) for i in [i + 1, j + 1, k + 1]))
    s = 0
    for i in xrange(size ** 2):
        for j in xrange(size):
            frequency_matrix[i, j] = count_occurrences(data, patterns[s])
            s += 1
    return frequency_matrix


if __name__ == '__main__':
#    array_string = ' '.join(str(x) for x in DATA)
#    print array_string
    matrix = gen_2d_frequency_matrix(DATA, SIZE)
    print matrix, '\n'
    matrix = gen_3d_frequency_matrix(DATA, SIZE)
    print matrix
