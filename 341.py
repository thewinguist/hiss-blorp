#mat = [[0,1],[1,0]]
#mat = [[0,0,0],[0,1,1]]
mat = [[0,0,1],
       [1,1,1],
       [0,0,0]]

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        counts = [0] * len(mat)
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                 if mat[i][j] == 1: counts[i] += 1

        max1 = max(counts)
        index = counts.index(max1)

        answer = [index, max1]
        return(answer)


