tup = (1,2,3,4,5,6,7)

print(tup.index(2)) #gives index of first occurence

print(tup.count(3)) #gives count of 3 in tuple

#Q- WAP to input three movie names and store them in a list 

movie1= input("enter movie1 : ")
movie2= input("enter movie2 : ")
movie3= input("enter movie3 : ")

#list=[movie1,movie2,movie3] OR
list=[]
list.append(movie1)
list.append(movie2)
list.append(movie3)

print(list)

#Q check if list is  palindrome
l1 = [1,2,1]
l2= l1.copy() #mak a copy of l1 
l2.reverse() #reverse that copy
#check if same , returns true if it is palindrome else false
if(l1==l2):
    print('yes Plaindrome')
else:
    print('not palindrome')    


#Q- count the students with 'A' grade in a tuple

grades = ('A','B','C','A','C','A','D')

print("total A graders = ",grades.count('A'))

#Q- store the above values in a list and sort it

grades = ['A','B','C','A','C','A','D']

grades.sort()
print( ) 
print(grades)

