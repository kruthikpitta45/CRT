'''li = []
ress = [5,4,3,2,1]
for i in range(len(ress)):
    if i%2!=0:
        lm = ress[i]*ress[i]
        li.append(lm)
print(li)'''
"""
import string
string  = "python programming"
print(string *2)
"""
"""
n = int(input())
x = " *"
for i in range(1,n+1):
    print(" "*(n-i)+x*i)
"""
"""
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):    
    print(" "*(n-i)+"* "*i)
    """
"""
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))
    """
#pascal triangle
"""
n = int(input())
for i in range(1,n+1):
    num = [1]
    for j in range(i):
        print(num[j],end=" ")
        num.append(num[j] * (i-j) // (j+1))     
        num.append(1)
    print()    """

n = int(input())
for i in range(1, n+1):
    print("*" *i +" "*(2*(n-i))+i*"*")
    for j in range(n,0,-1):
        print("*" *j +" "*(2*(n-j))+j*"*")
    

