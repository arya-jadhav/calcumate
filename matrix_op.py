def extractSubMatrix(matrix, pivot, column):  #pivot always first row for now
    size=len(matrix)
    sub_mat = [0]*(size-1)
    for i in range(len(sub_mat)):
        sub_mat[i] = [0] * (size-1)

    for i in range(1, size): #1,2
        counter = 0
        for col in range(size):
            if col == (column-1):
                continue
            else:           #add to correct position in sub matrix
                sub_mat[i-1][counter] = matrix[i][col]
                counter +=1
    return sub_mat


def calc_determinant(matrix):
    if len(matrix)==2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        res=0
        i=1
        for j in range(1, len(matrix)+1):  #1, 2,...n
            res += ((-1)**(i+j))*matrix[i-1][j-1]*calc_determinant(extractSubMatrix(matrix, i, j))
        return res

def calc_multiply(m1, m2, row1, col1, row2, col2):
    res = []
    res = [0] * row1
    for i in range(len(res)):
        res[i] = [0] * col2

    for i in range(row1):
        for j in range(col2):
            res[i][j] = sum([m1[i][x] * m2[x][j] for x in range(col1)])

    for i in range(len(res)):
        print("|", end=" ")
        for j in range(len(res[i])):
            print(res[i][j], end=" ")
        print("|")
# matrix=[[4, 5, 6, 7],[8, 9, 6, 5],[0, 7, 6, 6],[1, 2, 1, 0]]
#
# if __name__ == "__main__":
#     print(determinant(matrix))
