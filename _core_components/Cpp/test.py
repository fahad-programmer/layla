from cpp_func import greet_main, greet_h
import timeit

cpp = (timeit.timeit('greet_main().decode("utf-8")',
                     setup="from cpp_func import greet_main",
                     number=1000))
p = (timeit.timeit('greet()', setup="from main import greet", number=1000))
c = (timeit.timeit('greet_h().decode("utf-8")',
                   setup="from cpp_func import greet_h",
                   number=1000))

print(c)
print(cpp)
print(p)
