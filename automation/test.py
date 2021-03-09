
from movies import get_trending_movies
import timeit


python_m = timeit.timeit("get_trending_movies()", number=1, setup="from movies_1 import get_trending_movies")
c_m = timeit.timeit("get_trending_movies()", number=1, setup="from movies import get_trending_movies")

print(c_m)
print(python_m)

print(f"C is {c_m/python_m}x times faster than python")