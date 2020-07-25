from collections import defaultdict


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
    	vals = defaultdict(int)
    	for num in nums:
        	vals[num] += 1
   	 
    	for num in vals:
        	if vals[num] == 1:
            	return num