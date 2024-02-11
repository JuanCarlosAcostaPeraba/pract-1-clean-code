#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 9 11:30:00 2024

@author: Juan Carlos Acosta Perabá

This is a clean code version of the dirty.py file.
"""

class Class_array_n_to_m:
	"""
	A class representing an array of numbers from n to m.

	Attributes

	n : int
		The first number of the array.

	m : int
		The last number of the array.

	Methods

	get_array()
		Returns the array of numbers from n to m.

	get_min()
		Returns the minimum value of the array.

	get_max()
		Returns the maximum value of the array.

	get_mean()
		Returns the mean of the array.
	"""

	def __init__(self, n, m):
		self.array_n_to_m = [i for i in range(n, m)]
	
	def get_array(self):
		return self.array_n_to_m
	
	def get_min(self):
		return min(self.array_n_to_m)
	
	def get_max(self):
		return max(self.array_n_to_m)
	
	def get_mean(self):
		return sum(self.array_n_to_m)/len(self.array_n_to_m)

start_array_1 = 0
end_array_1 = start_array_2 = 100
end_array_2 = 200

object_array_0_to_100 = Class_array_n_to_m(start_array_1, end_array_1)
object_array_100_to_200 = Class_array_n_to_m(start_array_2, end_array_2)

array_0_to_100 = object_array_0_to_100.get_array()
array_100_to_200 = object_array_100_to_200.get_array()

sum_arr0to100_arr100to200 = [element1 + element2 for element1, element2 in zip(array_0_to_100, array_100_to_200)]
print("a1 + a2 =", sum_arr0to100_arr100to200, "\n")

difference_arr100to200_and_arr0to100 = [element2 - element1 for element1, element2 in zip(array_0_to_100, array_100_to_200)]
print("a2 - a1 =", difference_arr100to200_and_arr0to100, "\n")

print('Array 0 to 100 -> minimum: ', object_array_0_to_100.get_min())
print('Array 0 to 100 -> maximum: ', object_array_0_to_100.get_max())
print('Array 0 to 100 -> mean: ', object_array_0_to_100.get_mean())
print('Array 100 to 200 -> minimum: ', object_array_100_to_200.get_min())
print('Array 100 to 200 -> maximum: ', object_array_100_to_200.get_max())
print('Array 100 to 200 -> mean: ', object_array_100_to_200.get_mean())
print('Array 0 to 100 + Array 100 to 200 -> Array minimum: ', min(sum_arr0to100_arr100to200))
print('Array 0 to 100 + Array 100 to 200 -> maximum: ', max(sum_arr0to100_arr100to200))
print('Array 0 to 100 + Array 100 to 200 -> mean: ', sum(sum_arr0to100_arr100to200)/len(sum_arr0to100_arr100to200))
print('Array 100 to 200 - Array 0 to 100 -> Array minimum: ', min(difference_arr100to200_and_arr0to100))
print('Array 100 to 200 - Array 0 to 100 -> maximum: ', max(difference_arr100to200_and_arr0to100))
print('Array 100 to 200 - Array 0 to 100 -> mean: ', sum(difference_arr100to200_and_arr0to100)/len(difference_arr100to200_and_arr0to100))

