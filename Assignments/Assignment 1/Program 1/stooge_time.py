# Name: Pranav Prabhu
# Date: 04/11/2022
# Class: CS325

import random
import time

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
	print("\t  n\t\t\ttime(sec)\n----------------------------------------------")
   
	for n in range(50, 701, 50):
		array = []
      
		for i in range(1, n+1):
			array.append(random.randint(0, 10000))
		
		begin = time.time()
		stooge_sort(array, 0, len(array) - 1)
		end = time.time()
		print("\t", n, "\t\t", end - begin)
  
main()