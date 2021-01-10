import timeit
# print(greet().decode('utf-8'))
from core_func import greet, current_date


c = timeit.timeit("current_date().decode('utf-8')", setup='from core_func import current_date', number=5)
p = timeit.timeit('current_date()', setup='from main import current_date', number=5)

print(f"C is {p/c}x times faster than python")
print(greet().decode('utf-8'))
print(current_date().decode('utf-8'))