# Name: Pranav Prabhu
# Date: 04/11/2022
# Class: CS 325

import random
import time

def merge(array, begin, middle1, middle2, end):
	left_arr = array[begin : middle1]
	middle_arr = array[middle1 : middle2 - 1]
	right_arr = array[middle2 - 1 : end]
	
	left_arr.append(float("inf"))
	middle_arr.append(float("inf"))
	right_arr.append(float("inf"))
	
	left_index = middle_index = right_index = 0

	for i in range(begin, end):
		left_arr_index = left_arr[left_index]
		middle_arr_index = middle_arr[middle_index]
		right_arr_index = right_arr[right_index]

		minimum_value = min([left_arr_index, 	 
    middle_arr_index, right_arr_index])

		if (minimum_value == left_arr_index):
			array[i] = left_arr_index
			left_index += 1
		elif (minimum_value == middle_arr_index):
			array[i] = middle_arr_index
			middle_index += 1
		else:
			array[i] = right_arr_index
			right_index += 1

def merge_sort(array, begin, end):
	if (end - begin < 2): return array
	else:
		middle1 = begin + ((end - begin) // 3)
		middle2 = begin + 2 * ((end - begin) // 3) + 1

		merge_sort(array, begin, middle1)
		merge_sort(array, middle1, middle2)
		merge_sort(array, middle2, end)
		merge(array, begin, middle1, middle2 + 1, end)
		
		return array

def main():  
	print("\t  n\t\t\ttime(sec)\n---------------------------------------------")

	for n in range(5000, 50001, 5000):
		array = []
		
		for i in range(1, n+1):
			array.append(random.randint(0, 10000))			# Method 1
			#array.append(random.randrange(0, 10001))		# Method 2
			
		begin = time.time()
		merge_sort(array, 0, len(array))
		end = time.time()
		print("\t", n, "\t\t", end - begin)

main()