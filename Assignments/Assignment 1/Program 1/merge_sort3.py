# Name: Pranav Prabhu
# Date: 04/11/2022
# Class: CS 325

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
	# if len(array[begin : end]) < 2: return array

	if end - begin < 2: return array
	else:
		middle1 = begin + ((end - begin) // 3)
		middle2 = begin + 2 * ((end - begin) // 3) + 1

		merge_sort(array, begin, middle1)
		merge_sort(array, middle1, middle2)
		merge_sort(array, middle2, end)
		merge(array, begin, middle1, middle2 + 1, end)
		return array

def main():
	data_file = open("data.txt", "r")
	rows = data_file.readlines()
	array = []

	for line in rows:
		split_arr = line.split()
		for num in split_arr:
			array.append(int(num.strip()))

	value = array[0]
	index = 0
	counter = 0
  
	while index < len(array):
		if counter == 0:
			num_arr = array[index + 1 : value + 1]
      
			merge_sort(num_arr, 0, len(num_arr))
      
			for i in range(0, len(num_arr)):
				print(num_arr[i], end=' ')
			print(" ")
      
			counter += 1
			index += value				# index = 12
			value = array[index + 1]	# value = array[13] = 20
      
		else:
			num_arr = array[index + 2 : index + value + 2]
      
			merge_sort(num_arr, 0, len(num_arr))
      
			for i in range(0, len(num_arr)):
				print(num_arr[i], end=' ')
			print(" ")
      
			counter += 1
			index += value + 1			# index = 12 + 20 = 33
			if (index >= len(array) - 1): break
      
			value = array[index + 1] 	# value = array[34] = 9
      		
	data_file.close()

main()

'''
Resources: https://www.geeksforgeeks.org/3-way-merge-sort/#:~:text=A%20variant%20of%20merge%20sort%20is%20called%203-way,the%20arrays%20to%20subarrays%20of%20size%20one%20third.
'''