def sum_odd_nums(nums):
	total = 0 
	for xyz in nums:
		if xyz % 2 != 0:
			total += xyz
	return total


print(sum_odd_nums([1,2,3,4,5,6,7]))
