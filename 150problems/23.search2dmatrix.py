class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        print("Matrix: ", matrix)
        rows = len(matrix)
        print("Rows before loop: ", rows)
        cols = len(matrix[0])
        print("Cols before loop: ", cols)


        left = 0
        right = rows * cols - 1


        while left <= right:
            mid = left + (right - left) // 2
            print("Mid: ", mid)

            row = mid // cols
            col = mid % cols
            print("Row in loop: ", rows)
            print("Col in loop: ", col)


            if matrix[row][col] == target:
                print("matrix[row][col]: ", matrix[row][col])
                return True
            
            elif matrix[row][col] < target:
                print("matrix[row][col]: ", matrix[row][col])
                left = mid + 1
                print("left", left)

            else:
                right = mid - 1
                print("right", right)
        return False
    

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
solution.searchMatrix(matrix, target)