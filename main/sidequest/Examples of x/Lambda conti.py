# # 1. Double a number
# double = lambda x: x * 2
# print(double(5))  # ➜ 10
#
# # 2. Add two numbers
# adder = lambda a, b: a + b
# print(adder(3, 4))  # ➜ 7
#
# # 3. Sort by second item
# pairs = [(1, 'a'), (3, 'c'), (2, 'b')]
# pairs.sort(key=lambda x: x[1])
# print(pairs)  # ➜ [(1, 'a'), (2, 'b'), (3, 'c')]

# funcs = []
# results = []
# x =10
#
# for i in range(3):
#     funcs.append(lambda x: x + i)
# results = [f(10) for f in funcs]
# print(results)

#
# funcs.append(lambda x: [x + i for i in range(3)])
# results = [f(10) for f in funcs]
# print(results)
# this creates only one lambda functon that returns 3 seprate vals not 3 seprate functs that retunr one vale each
# funcs.append(lambda x: [x + i for i in range(3)])
# results = [f(10) for f in funcs]
# print(results)

funcs = [] # stores all the functions
for i in range(10):
    funcs.append(lambda x, i=i: x + i) #
results = [f(10) for f in funcs]
print(results)

