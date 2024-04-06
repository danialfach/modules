print("module main", __file__)

import calculate
print("module calculate", calculate.__file__)

import random
print("module random", random.__file__)

data1 = "Danial Fachrudin"
print(f"var: data1, data: {data1}, type: {type(data1).__name__}")

data2 = 24 * 7
print(f"var: data2, data: {data2}, type: {type(data2).__name__}")
