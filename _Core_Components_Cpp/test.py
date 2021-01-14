from cpp_func import addition, subtract, divide, multiply
import timeit

# cpp = timeit.timeit(
#     "searching_google(b'who is the prime minister of pakistan')",
#     setup="from cpp_func import searching_google",
#     number=2)
# p = timeit.timeit("searching_google('who is the prime minister of pakistan')",
#                   setup="from main import searching_google",
#                   number=2)

# print(f"cpp is {p/cpp} times faster than python")

main_list = "please divide 55 with 95 and 966"
print(addition(main_list))
print(subtract(main_list))
print(divide(main_list))
print(multiply(main_list))