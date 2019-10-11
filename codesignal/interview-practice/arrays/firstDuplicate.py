"""
Given an array 'a' that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the 
minimal index. In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than 
the second occurrence of the other number does. If there are no such elements, 
return -1.

Example:
For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a 
smaller index than the second occurrence of 2 does, so the answer is 3.

For a = [2, 2], the output should be firstDuplicate(a) = 2;
For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1
"""
def firstDuplicate(a):
	my_set = set()
	for value in a:
		if value in my_set:
			return value
		else:
			my_set.add(value)

	return -1



a = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(a))

a = [2, 2]
print(firstDuplicate(a))

a = [2, 4, 3, 5, 1]
print(firstDuplicate(a))

a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]
print(firstDuplicate(a))

a = [1, 1, 2, 2, 1]
print(firstDuplicate(a))

