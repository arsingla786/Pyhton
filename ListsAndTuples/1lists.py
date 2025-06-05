marks= [98.6,34,56.7,34.9]

print(marks)
print(type(marks)) #-->list

#we can also print element of a particular index starting from 0
print("marks 1 = ",marks[0])
 
#it can store elemets of different types like int , float, strings

student=["arun",78,"vijay"]
print(len(student))
print(student[0])

student[0]="arjun"
print(student) #this shows that list is mutable , means it changes can be made unlike string

'''• LIST SLICING
••to access a part of a list 
list_name[starting_index,ending_index] ending index not included'''

numbers =[1,2,3,4,5,6,7,8,9]

print(numbers[1:4])

print(numbers[:4]) #same as [0 : 4]

print(numbers[1:]) #same as [1:len(numbers)]

print(numbers[-3:-1])


