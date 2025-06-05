#tuples are same as lists but are immutable (cant be changed) like strings 

tup = (1,2,3,4)
tup2 = () #empty tupl is valid
print(type(tup))
print(tup)

tup2 = () #empty tupl is valid
print(tup2)

tup3 = (1,) #right syntax to declare tupl with one elment
print(tup3)

tup4=(1)
print(tup4) #treated as an int not a tuple

#SLICING works same as lists 
print(tup[1:])

print(tup[0:3])

