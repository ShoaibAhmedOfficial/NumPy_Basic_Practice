import timeit
import numpy as np

# Normal Python list comprehension
print(timeit.timeit('[j**4 for j in range(1,9)]', number=10000))

# NumPy version
print(timeit.timeit('np.arange(1,9)**4', number=10000, setup='import numpy as np'))
