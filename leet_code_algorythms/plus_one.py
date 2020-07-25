class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
    	# change ints into str
    	for i in range(len(digits)):
        	digits[i] = str(digits[i])
   	 
    	# operations to get str(starting num + 1)
    	temp = ''.join(digits)
    	temp = int(temp)
    	temp += 1
    	temp = str(temp)
   	 
    	res = []
    	for j in range(len(temp)):
        	res.append(int(temp[j]))
    	return res
