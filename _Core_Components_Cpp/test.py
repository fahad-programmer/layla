# import timeit
# from cpp_func import addition
# from main import addition_main

# main_q = "Please Add 5 7 99 66 44 55"

# start = timeit.default_timer()
# print(addition(main_q).decode('UTF-8'))
# end = timeit.default_timer()

# start2 = timeit.default_timer()
# print(addition_main(main_q))
# end2 = timeit.default_timer()

# print(f"The Execution Took {end - start}")
# print(f"The Execution Took {end2 - start2}")

# c = end - start

# py = end2 - start2

# print(f"C++ is {py/c}x times faster")
import re
from cpp_func import maths_func

query = "Please Find tan Of 25"
print(maths_func(query))

# print(maths_func("Please Find round off Of 9.33"))