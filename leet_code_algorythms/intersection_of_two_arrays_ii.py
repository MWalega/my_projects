from collections import defaultdict


class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	if len(nums2) > len(nums1):
        	return self.intersect(nums2, nums1)
   	 
    	nums2_dict = defaultdict(int)
    	for num in nums2:
        	nums2_dict[num] += 1
       	 
    	res = []
    	for num in nums1:
        	if nums2_dict[num] > 0:
            	res.append(num)
            	nums2_dict[num] -= 1
   	 
    	return res
