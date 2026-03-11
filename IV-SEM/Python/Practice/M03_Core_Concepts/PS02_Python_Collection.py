a = [1,2,3,4,5]
print(a)

print(a[0])
print(a[1]) 
a.append(6)
print(a)
""" SETS """
#sets caanot have duplicate values
s = {1,2,3,4,5}     
print(s)
s.add(6)        
print(s)
s.add(6)
print(s)
s.add(7)

print(s)
s.remove(6)
print(s)
b = {4,5,6,7,8}
print(s.union(b))
print(s.intersection(b))
print(s.difference(b))
print(s.symmetric_difference(b))    
