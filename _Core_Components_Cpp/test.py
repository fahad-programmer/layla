from cpp_func import greet_main
import timeit

cpp = (timeit.timeit('date_time().decode("utf-8")',
                     setup="from cpp_func import date_time",
                     number=1))
p = (timeit.timeit('current_date()',
                   setup="from main import current_date",
                   number=1))
c = (timeit.timeit('current_date().decode("utf-8")',
                   setup="from core_func import current_date",
                   number=1))
c_cpp = (timeit.timeit('current_date_now().decode("utf-8")',
                       setup="from cpp_func import current_date_now",
                       number=1))

print(c)
print(cpp)
print(p)

print(
    f"C++ is {p/cpp} times faster than python and {c/cpp} times faster than C and {c_cpp/cpp} times faster than c++(cython)"
)
