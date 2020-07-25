class Solution:
	def small_square_valid(self, small_square: List[List[str]]) -> bool:
        	nums_set = set()
        	for lst in small_square:
            	for char in lst:
                	if char != '.':
                    	if char not in nums_set:
                        	nums_set.add(char)
                    	else:
                        	return False
        	return True
    
	def isValidSudoku(self, board: List[List[str]]) -> bool:
    	# checking small squares
    	for i in range(0, len(board), 3):
        	for j in range(0, len(board), 3):
            	rows = [board[x] for x in range(i, i+3)]
            	small_square = [row[j:j+3] for row in rows]
            	if not self.small_square_valid(small_square):
                	return False
           	 
    	# checking rows and cols
    	for i in range(len(board)):
        	row_set = set()
        	col_set = set()
        	for j in range(len(board)):
            	if board[i][j] in row_set or board[j][i] in col_set:
                	return False
            	else:
                	if board[i][j] != '.':
                    	row_set.add(board[i][j])
                	if board[j][i] != '.':
                    	col_set.add(board[j][i])
   	 
    	return True

