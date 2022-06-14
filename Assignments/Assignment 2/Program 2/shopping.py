# Name: Pranav Prabhu
# Class: CS 325
# Date: 04/18/22

def shopping(val, wt, W, n):
	#array = [[0 for x in range(W + 1)] for x in range(n + 1)]          # Method 1 (using list comprehension): fill 2D array with 0s
   
	array = []
	
	for i in range(n + 1):                  # Method 2 (using nested for-loops): fill 2D array with 0s
		array.append([])
		for j in range(W + 1):
			array[i].append(0)
	
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0: array[i][w] = 0
			elif wt[i - 1] <= w:
				array[i][w] = max(val[i - 1] + array[i - 1][w - wt[i - 1]], array[i - 1][w])
			else: array[i][w] = array[i - 1][w]

	result = array[n][W]
	w = W

	wt_array = []
	for i in range(n, 0, -1):
		if result <= 0: break

		if result == array[i - 1][w]: continue
		else:
			wt_array.append(i)
			result -= val[i - 1]
			w -= wt[i - 1]
	
	return array[n][W]

def find_path(val, wt, W, n):   
	array = []
	
	for i in range(n + 1):
		array.append([])
		for j in range(W + 1):
			array[i].append(0)
	
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0: array[i][w] = 0
			elif wt[i - 1] <= w:
				array[i][w] = max(val[i - 1] + array[i - 1][w - wt[i - 1]], array[i - 1][w])
			else: array[i][w] = array[i - 1][w]

	result = array[n][W]
	w = W

	wt_array = []
	for i in range(n, 0, -1):
		if result <= 0: break

		if result == array[i - 1][w]: continue
		else:
			wt_array.append(i)
			result -= val[i - 1]
			w -= wt[i - 1]
			
	wt_array.sort()
	for i in range(len(wt_array)): print(wt_array[i], end=' ')
	print(" ")

def main():
	data_file = open("shopping.txt", "r")
	rows = data_file.readlines()
	array = []
	
	for line in rows:
		split_arr = line.split()
		for num in split_arr:
			array.append(int(num.strip()))
	
	test_cases = array[0]
	num_of_items = array[1]
	test_count = 1
	index = 0
	total = 0
	
	while test_count <= test_cases:
		num_of_items = array[1]
		total = 0
		
		items_array = array[index + 2 : index + 2 + (num_of_items * 2)]
		new_items_array = [items_array[i : i + 2] for i in range(0, len(items_array), 2)]
		#print("\nNew Items Array: ", new_items_array)
	
		#price = [new_items_array[i][0] for i in range(0, len(new_items_array))]          # Method 1: filling price array
		price = [i[0] for i in new_items_array]                                           # Method 2: filling price array
		
		#weight = [new_items_array[i][1] for i in range(0, len(new_items_array))]         # Method 1: filling weight array
		weight = [i[1] for i in new_items_array]                                          # Method 2: filling weight array
	
		#print("Price: ", price)
		#print("Weight: ", weight, "\n")
	
		fam_index = index + 2 + (num_of_items * 2)
		fam_mem_count = array[fam_index]
		family = array[fam_index + 1 : fam_index + fam_mem_count + 1]
		#print("\nFamily: ", family, "\n")

		print("Test Case ", test_count)
				
		for member in family:
			total += shopping(price, weight, member, array[1])
		print("Total Price ", total)
		
		count = 1
		for member in family:
			print(count, ": ", end=' ')
			find_path(price, weight, member, array[1])
			count += 1
			
		print(" ")

		test_count += 1
	
		del array[1 : (index + 2 + (num_of_items * 2)) + fam_mem_count + 1]

	data_file.close()

main()

'''
Resources: https://www.geeksforgeeks.org/printing-items-01-knapsack/
'''