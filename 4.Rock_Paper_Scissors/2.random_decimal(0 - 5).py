# Print a random decimal between 0 and 5.

import random
rand_float = random.random()   # only generates floating point numbers between 0.0000... and 0.9999...
rand_float *= 5
print(rand_float) 