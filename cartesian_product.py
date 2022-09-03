import numpy

def cartesian_product(*arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)


X = numpy.array([-1, 0, 1])
Y = numpy.array([-1, 0, 1])

print(cartesian_product(X, Y))
