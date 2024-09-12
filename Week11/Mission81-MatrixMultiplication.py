#START CODING FROM HERE
#======================

#define the function to multiply matrix A with matrix B, store
#the product in matrix C and return
def matrix_multiplication(A,B):
    C = []
    #Add your code here
    for row in A:
        sum = 0
        for i in range(len(row)):
            result = row[i] * B[i]
            sum += result
        C.append(sum)
    
    return C #do not remove this line
       
#Define matrix A as a nested list and matrix B as a list
#remove these statements when submitting in Coursemology
A = [[99,9,9],[88,9,9],[77,9,99]]
B = [1,0,0]

#Do not remove the next line that calls the function
C = matrix_multiplication(A,B)

#Display the result
print(C)

# matrix_multiplication([[1,2,3],[4,5,6],[7,8,9]],[1,2,3])

# [14, 32, 50]

# matrix_multiplication([[99,9,9],[88,9,9],[77,9,99]],[1,0,0])

# [99, 88, 77]