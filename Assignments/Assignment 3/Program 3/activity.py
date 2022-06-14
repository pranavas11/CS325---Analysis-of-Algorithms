# Name: Pranav Prabhu
# Class: CS 325
# Date: 05/01/22

def merge_sort(array, size):
	if len(array) > 1:
		middle = len(array) // 2
		left = array[:middle]
		right = array[middle:]

		merge_sort(left, len(left))
		merge_sort(right, len(right))

		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1

def insertion_sort(activity, start, finish, size):
	act_key = start_key = finish_key = j = 0
	
	for i in range(1, size):
		act_key = activity[i]
		start_key = start[i]
		finish_key = finish[i]
		j = i - 1
				
		while j >= 0 and start[j] > start_key:
			activity[j+1] = activity[j]
			start[j+1] = start[j]
			finish[j+1] = finish[j]
			j -= 1
		
		activity[j+1] = act_key
		start[j+1] = start_key
		finish[j+1] = finish_key

'''
activity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
start = [1, 3, 0, 5, 3, 4, 6, 9, 8, 2, 12]
finish = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
insertion_sort(activity, start, finish, len(activity))
print(activity, "\n", start, "\n", finish, "\n\n\n")
'''

def num_activities(activity, start, finish, size):
	max = 1
	i = size - 1

	for j in range(size-2, -1, -1):
		if finish[j] <= start[i]:
			max += 1
			i = j

	print("Maximum number of activities = ", max)
	return max

def activity_selection(activity, start, finish, size, max_activities):
	selected_array = []
	i = size - 1
		
	selected_array.append(activity[i])

	for j in range(size-2, -1, -1):
		if finish[j] <= start[i]:
			selected_array.append(activity[j])
			i = j

	merge_sort(selected_array, max_activities)
	for k in range(0, len(selected_array)): print(selected_array[k], end=' ')
	print(" ")
	
def main():
	array = []
	
	data_file = open("act.txt", "r")
	rows = data_file.readlines()
	
	for line in rows:
		split_arr = line.split()
		for num in split_arr:
			array.append(int(num.strip()))
	
	data_file.close()

	array_length = set = 0

	while array_length != len(array):
		set += 1
		print("Set", set)
		
		num_of_activities = array[0]
		activity_set = array[1 : (num_of_activities * 3) + 1]
		#print("\n", activity_set)
		activity = activity_set[0 : len(activity_set) : 3]
		start = activity_set[1 : len(activity_set) : 3]
		finish = activity_set[2 : len(activity_set) : 3]
		#print("\n", activity)
		#print("\n", start)
		#print("\n", finish)
		
		insertion_sort(activity, start, finish, num_of_activities)
		max_activities = num_activities(activity, start, finish, num_of_activities)
		activity_selection(activity, start, finish, num_of_activities, max_activities)
		print(" ")
	
		del array[0: (num_of_activities * 3) + 1]
		#print("\n\n\n", array)

main()

'''
Resources:
https://www.geeksforgeeks.org/merge-sort/
https://www.geeksforgeeks.org/insertion-sort/
'''