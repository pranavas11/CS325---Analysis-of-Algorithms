# Name: Pranav Prabhu
# Date: 04/11/2022
# Class: CS325

def stooge_sort(array, start, end):
	if start >= end: return

	if array[start] > array[end]:
		temp = array[start]
		array[start] = array[end]
		array[end] = temp

	length = end - start + 1
	
	if length >= 3:
		middle = (int)(length / 3)
		stooge_sort(array, start, end - middle)
		stooge_sort(array, start + middle, end)
		stooge_sort(array, start, end - middle)

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
      
			stooge_sort(num_arr, 0, len(num_arr) - 1)
      
			for j in range(0, len(num_arr)):
				print(num_arr[j], end = ' ')
			print(" ")
      
			counter += 1
			index += value				# index = 12
			value = array[index + 1]	# value = array[13] = 20
      
		else:
			num_arr = array[index + 2 : index + value + 2]
      
			stooge_sort(num_arr, 0, len(num_arr) - 1)
      
			for j in range(0, len(num_arr)):
				print(num_arr[j], end = ' ')
			print(" ")
      
			counter += 1
			index += value + 1			# index = 12 + 20 = 33
      
			if (index >= len(array) - 1): break
      
			value = array[index + 1] 	# value = array[34] = 9

	data_file.close()

main()

# Citation: https://www.geeksforgeeks.org/python-program-for-stooge-sort/