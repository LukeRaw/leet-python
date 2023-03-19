# ROTATE IMAGE IN PROGRESS

# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
        
#         # 00, 03, 33, 30
#         # 01, 13, 32, 20
#         # 02, 23, 31, 10
#         # 03, 33, 30, 00
        
#         # 11, 12, 22, 21
        
#         rotation_matrix = [
#             [(0,0), (0,3), (3,3), (3,0)],
#             [(0,1), (1,3), (3,2), (2,0)],
#             [(0,2), (2,3), (3,1), (1,0)],
#             [(0,3), (3,3), (3,0), (0,0)],
#             [(1,1), (1,2), (2,2), (2,1)]
#         ]
        
#         for row in rotation_matrix:
#             # temp = row[0]
#             # temp = matrix[row[1][0]][row[1][1]]
#             temp = matrix[row[0][0]][row[0][1]]
#             for i in range(len(row)-1):
#                 print(i)
#                 print(matrix[])
#                 temp = matrix[row[i][0]][row[i][1]]
#                 # temp = matrix[row[i+1][0]][row[i+1][1]]
#                 if i % 2 == 0:
#                     # temp = matrix[row[i][0]][row[i][1]]
#                     temp_2 = matrix[row[i+1][0]][row[i+1][1]]
#                     matrix[row[i+1][0]][row[i+1][1]] = temp
#                 else:
#                     temp = matrix[row[i][0]][row[i][1]]
#                     matrix[row[i+1][0]][row[i+1][1]] = temp_2
#                 # temp = matrix[row[i+1][0]][row[i+1][1]]
#                 # temp = matrix[row[i+1][0]][row[i+1][1]]