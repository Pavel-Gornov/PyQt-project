mat = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [2, 2, 2, 2],
       [2, 2, 2, 2]]


def transpose(mat1):
    new = []
    for i in range(len(mat1[0])):
        new.append([])
        for j in range(len(mat1)):
            new[i].append(mat1[j][i])
    return new


def reverse(mat2):
    new = []
    for i in range(len(mat2)):
        new.append([])
        for j in range(len(mat2[0])):
            new[i].append(mat2[i][len(mat2[0]) - j - 1])
    return new


print(*mat, sep='\n')
l = transpose(mat)
l = reverse(l)
print()
print(*l, sep='\n')
print(len(mat[0]))
print(len(mat))
