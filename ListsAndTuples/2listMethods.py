list = [2,4,3,1]

list.append(5) #adds an element at last
print(list)

list.sort()
print(list) #sorts the list in ascending order

list.sort(reverse= True) #sorts in descending order
print(list)

list.reverse()#reverse the list
print(list) 

list.insert(3,23) #inserts 23 at 3rd index
print(list)

list.remove(23) #rmoves the first occurence of 23 
print(list)

list.pop(2) #removes element at index 2

print(list)  

list[1]=10 #edit any elment in list
print(list)
#these functions make changes in the real list (mutating)








