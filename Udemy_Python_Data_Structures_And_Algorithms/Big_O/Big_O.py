# # Big O

# Comparing 2 sets of code (which is better?) mathematically about how efficient they run

# ## Time Complexity

# - measure Space complexity

# Time does not have to equal space complexity just depends on the situation

# ## Big O Worst Case

# - Best case is Omega Ω
# - Average case is Theta θ
# - Worst case is Omicron (O)

# ### O(n)


def print_items(n):
	for i in range(n):
		print(i)

print_items(10)

# O(n)

# ```

# set amount of times that it will run

# ### Drop Constants O(10n), 0(9n)… == O(n)


def print_items(n):
	for i in range(n):
		print(i)

	for j in range(n):
		print(j)

print_items(10)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# ```

# Both will run 0-9, 0-9 for n amount of times
# n + n = 2n
# O(2n) ***Drop the Constant***
# == O(n)

# ### O(n^2)

# ```python
def print_items(n):
	for i in range(n):
		for j in range(n):
			print(i, j)

# print_items(10)

# 0 0
# 0 1
# 0 2
# 0 3
# 0 4
# 0 5
# 0 6
# 0 7
# 0 8
# 0 9
# 1 0
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 2 0
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# 2 6
# ...
# ...
# ...
# 8 5
# 8 6
# 8 7
# 8 8
# 8 9
# 9 0
# 9 1
# 9 2
# 9 3
# 9 4
# 9 5
# 9 6
# 9 7
# 9 8
# 9 9
# ```

# *loop inside of a loop (nested)

# n * n = n^2

# O(n^2)

# ### Drop Non-Dominants

# ```python
# def print_items(n):
# 	for i in range(n):
# 		for j in range(n):
# 			print(i, j)

# 	for k in range(n):
# 		print(k)

# print_items(10)
# ```

# Nested loop with an additional non nested loop

# Nested loop ran O(n^2)

# Non nested loop ran O(n)

# O(n^2) + O(n) = O(n^2 + n)

# The exponent is significant and the standalone is too small to make a difference

# the standalone is dropped

# == O(n^2)

# ### O(1) *Most Eff*i*cient*


def add_items(n):
	return n + n + n

add_items(10)


# One operation… doesn't matter if its 1 or more

# *constant time

# as the number of operations increase, the time stays constant

# == O(1)

# ### O(log n)

# Sorting algo where you cut in half multiple times

# ### Different Terms for Inputs


def print_items(a, b):
	for i in range(a):
		print(i)

	for j in range(b):
		print(j)

print_items(1, 10)


# Interview trick question ***

# for loop + for loop = O(n) + O(n) == O(2n) == O(n)

# This works when the parameter is the same!

# When the parameter is different it is now

# O(a) + O(b) == O(a + b)

# If the loop was nested it would be

# O(a) * O(b) == O(a * b)

# ### Big O of Lists

# O(n) the numbers of items in the list is n which is constant

# https://www.bigocheatsheet.com/

# O(n^2)

# - loop within a loop

# O(n)

# - proportional

# O(log n)

# - Divide and conquer

# O(1)

# - Constant
