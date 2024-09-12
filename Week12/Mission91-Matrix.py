#Programming I

#######################
#     Mission 9.1     #
#   MartrixMultiply   #
#######################

#Background
#==========
#Tom has studied about creating 3D games and wanted
#to write a function to multiply 2 matrices.
#Define a function MaxtrixMulti() function with 2 parameters.
#Both parameters are in a matrix format.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[2,0,0],
     [0,2,0],
     [0,0,2]]

#START CODING FROM HERE
#======================

#Create your function here

def matrixmult(A,B):
     result = []
     for i in range(len(A)):
          numlist = []
          for j in range(len(B[0])):
               sum = 0
               for k in range(len(B)):
                    sum += A[i][k] * B[k][j]
               numlist.append(sum)
          result.append(numlist)
            
     return result

   
#Do not remove the next line
matrixmult(A, B)

#3) For testing, print out the output
#   - Comment out before submitting
# expected: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]






