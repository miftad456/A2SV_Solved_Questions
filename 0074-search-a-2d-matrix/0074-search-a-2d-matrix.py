class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=left+(right-left)//2
            lif=0
            lis=len(matrix[mid])-1
            while lif<=lis:
                dim=lif+(lis-lif)//2
                if matrix[mid][dim]==target:
                    return True
                elif matrix[mid][dim]>target:
                    lis=dim-1
                else:
                    lif=dim+1
            else:
                if matrix[mid][dim]>target:
                    right=mid-1
                else:
                    left=mid+1
                lif=0
                lis=len(matrix[mid])-1
        else:
            return False
            
            