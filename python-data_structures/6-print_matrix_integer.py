#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(0, len(i)):
            if i != len(i)-1:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
        print()
