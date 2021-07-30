#sets are immutable,unordered,duplicates values are not allowed

a = {1,2,3.0,"sets"}
print(a)

#finding length by using len()
print(len(a))

#Finding type of a
print(type(a))

#Creating another way of set
b = {4,5,6,2.0}
c = set([1,2,3])
print(b)
print(c)

#methods in sets by using dir()
print(dir(a))            #we can perform accessing operations in set


#discard(),remove(),pop()

print(a.discard(3.0))
print(a)

#trying to remove not defined value in --a using discard()
print(a.discard(76))
print(a)

#remove()
print(b.discard(4))
print(b)

#removing undefined number from b using remove()
#print(b.remove(36))
#print(b)                #it will throw error

#pop()
c = {43,56,12,6.2,45}
print(c.pop())          #it will remove random number from the given set


#union()   || pipeline
print(a | b)
print(a.union(c))

#intersection &

print(a & b)            #common values in both
print(a.intersection(b))


#difference
print(a-b)
print(b-a)







