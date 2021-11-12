import random
size = input("Please enter the grid size i.e. 10 = 10x10 grid: ")
print(random.randint(0, 1))
#generate empty lists for grid
empty_lists = [[] for i in range(int(size))]

print(empty_lists)