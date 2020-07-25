class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
    	if len(nums) == 0:
        	return 0
   	 
    	len_ = 1
    	for i in range(1, len(nums)):
        	if nums[i] != nums[i-1]:
            	nums[len_] = nums[i]
            	len_ += 1
    	return len_
