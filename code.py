import numpy as np


print("This program deals with three-variable equatons, therefore should input three equations.")  #the user can input the coefficients by him/herself
print("Please input the first equation (A_00*x + A_01*y + A_02*z = A_03)")   
#get the first equation
A_00=float(input("A_00= "))
A_01=float(input("A_01= "))
A_02=float(input("A_02= "))
A_03=float(input("A_03= "))
print("Please input the second equation (A_10*x + A_11*y + A_12*z = A_13)")                         #get the second equation         
A_10=float(input("A_10= "))
A_11=float(input("A_11= "))
A_12=float(input("A_12= "))
A_13=float(input("A_13= "))
print("Please input the third equation (A_20*x + A_21*y + A_22*z = A_23)")                        #get the third equation
A_20=float(input("A_20= "))
A_21=float(input("A_21= "))
A_22=float(input("A_22= "))
A_23=float(input("A_23= "))
#print the equations to check the inputs equations
print("Your input equatons are: ",A_00,"x+",A_01,"y+",A_02,"z=",A_03,"  ",A_10,"x+",A_11,"y+",A_12,"z=",A_13,"  ",A_20,"x+",A_21,"y+",A_22,"z=",A_23)
augmented_matrix=np.array([[A_00,A_01,A_02,A_03],              #construct the array
                           [A_10,A_11,A_12,A_13],
                           [A_20,A_21,A_22,A_23]])

print("The original augmented matrix is: ")     #show the original input equations
print(augmented_matrix)
#==============================================================================================================
def swap(a,b):                                 #used to swap the two values
    return b,a

if augmented_matrix[0][0]==0:                  #check if the first coefficient [0,0] is zero,if it is 0 ,then we check [1][0]
    if augmented_matrix[1][0]==0:              #then check [1][0],if it's not 0 then swap row0 and row.,If it's also 0 ,then we swap row0 and row2
        for i in range(0,4):  #swap row1 and row0                 
            augmented_matrix[0][i],augmented_matrix[2][i]=swap(augmented_matrix[0][i],augmented_matrix[2][i])
    else:
        for i in range(0,4):  #swap row2 and row0
            augmented_matrix[0][i],augmented_matrix[1][i]=swap(augmented_matrix[0][i],augmented_matrix[1][i])
else:                                           #if augmented_matrix[0][0] is not zero, then we do nothing 
    pass
  
if augmented_matrix[0][0]!=0:                                  #I used this if statement to avoid the exception ,where all the first coefficients of the three row are 0.In that, this exception could make the program die, when all the three equations have no first coefficient. 
    ratio_01=augmented_matrix[1][0]/augmented_matrix[0][0]     #ratio_01 is the ratio of augmented_matrix[1][0] and augmented_matrix[0][0] 
    ratio_02=augmented_matrix[2][0]/augmented_matrix[0][0]     #ratio_02 is the ratio of augmented_matrix[2][0] and augmented_matrix[0][0]
    for i in range(4):                                         # elemination row 1 with row0 by ratio01 (make augmented_matrix[1][0] become 0)
        augmented_matrix[1][i]=augmented_matrix[1][i]-augmented_matrix[0][i]*ratio_01
     
    for i in range(4):                                         # elemination row 1 with row0 by ratio01 (make augmented_matrix[1][0] become 0)
        augmented_matrix[2][i]=augmented_matrix[2][i]-augmented_matrix[0][i]*ratio_02 
else:
    pass
  
#then start to address the second coefficient of row1 and row2.
if augmented_matrix[1][1]!=0 and augmented_matrix[2][1]!=0:       #eliminate row2 with row1 by ratio_12 when both the second coefficients of row2 and row1 are not 0
    ratio_12=augmented_matrix[2][1]/augmented_matrix[1][1]
    for i in range(4):
        augmented_matrix[2][i]=augmented_matrix[2][i]-augmented_matrix[1][i]*ratio_12
elif augmented_matrix[1][1]==0 and augmented_matrix[2][1]!=0:     #when augmented_matrix[1][1]==0 and augmented_matrix[2][1]!=0 ,swap row1 and row2, so that we can make the output to be an upper triangle.Also this elif will need no elimination ,in that, it already has one of the coefficient as 0
    for i in range(0,4):
            augmented_matrix[1][i],augmented_matrix[2][i]=swap(augmented_matrix[1][i],augmented_matrix[2][i])
else:                                                            #when augmented_matrix[1][1] augmented_matrix[2][1] areboth 0,or augmented_matrix[1][1]!=0 and augmented_matrix[2][1]==0,it need no eliminating and swapping. 
    pass
  
#test:print the augment matrix after gauss elimination
print("the augment matrix after gauss elimination:")
print(augmented_matrix)

#calculate x1,x2,x3
x=np.zeros(3)                                 #x[0]=x1的解  x[1]=x2  x[2]=x3的解
for i in range(0,3):                          #由經過高斯消去後的矩陣，由x3->x2->x1依序解出
    x_divide=augmented_matrix[2-i][3]         #每equation的係數乘上對應的x值加上y值
    for j in range (0,3):                     #每輪eq計算均會把每個x都算計去，如果當時對應的x還沒算，他就會是帶入0所以不影響               
        x_divide=x_divide-augmented_matrix[2-i][2-j]*x[2-j]
    x[2-i]=x_divide/augmented_matrix[2-i][2-i]

print("x:",x)



    
