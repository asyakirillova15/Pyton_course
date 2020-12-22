from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]
mixing = reduce(lambda num_1, num_2: num_1 * num_2, my_list)
print(mixing)
