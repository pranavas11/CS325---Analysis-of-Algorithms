# Name: Pranav Prabhu
# Class: CS 325
# Date: 04/18/22

import random
import time

def maximum_value(value1, value2):
	if value1 > value2: return value1
	else: return value2

def recursive_knapsack(val, wt, W, n):
	if n == 0 or W == 0: return 0

	if wt[n - 1] > W: return recursive_knapsack(val, wt, W, n - 1)
	else:
		return maximum_value(val[n - 1] + recursive_knapsack(val, wt, W - wt[n - 1], n - 1), recursive_knapsack(val, wt, W, n - 1))

def DP_knapsack(val, wt, W, n):
	#array = [[0 for x in range(W + 1)] for x in range(n + 1)]					# Method 1: fills 2D array with 0s as placeholder

	array = []

	for i in range(n + 1):							# Method 2: fills 2D array with 0s as placeholder
		array.append([])
      
		for j in range(W + 1):
			array[i].append(0)

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0: array[i][w] = 0
			elif wt[i - 1] <= w:
				array[i][w] = maximum_value(val[i - 1] + array[i - 1][w - wt[i - 1]], array[i - 1][w])
			else: array[i][w] = array[i - 1][w]

	return array[n][W]

def main():
	W = 100

	for n in range(10, 41, 5):
		val = []
		wt = []
		recurse_max = DP_max = 0
		
		for j in range(0, n):
			val.append(random.randint(1, 50))
			wt.append(random.randint(1, 30))

		recurse_begin = time.time()
		recurse_max = recursive_knapsack(val, wt, W, n)
		recurse_end = time.time()
		recurse_time_diff = recurse_end - recurse_begin

		DP_begin = time.time()
		DP_max = DP_knapsack(val, wt, W, n)
		DP_end = time.time()
		DP_time_diff = DP_end - DP_begin
		
		print("N = ", n, "\tW = ", W, "\tRec time = ", recurse_time_diff, "\tDP time = ", DP_time_diff, "\tRec max = ", recurse_max, "\tDP max = ", DP_max)

main()

'''
Citation: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''