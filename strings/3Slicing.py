#used to access a part of a string 
#used a lot in machine learning 

#format -> str[starting_index : ending_index] , but ending index is not printed
str="Hi! How are you?"

slicedStr = str[2 : 8]
print(slicedStr)

slicedStr2 = str[ : 5] #same as str[0 : 5]
print(slicedStr2)

slicedStr3 = str[1 : ] #same as str[1:len(str)]
print(slicedStr3)

'''NEGATIVE INDEX
#in python apart from other languages the indexing can be done in negative 
#string from backward from -1 ,-2,-3 .....

example - A P P L E the indexing is = (-5 -4 -3 -2 -1)'''

strNew = "apple"
print(strNew[-3 : -1])

#more functions

str = "i am a coder"
print(str.endswith("er")) #return true if string ends with er
print(str.capitalize())  #capitalize the first character
print(str.replace("a","e")) #replaces all a's in the string with e
print(str.find("m")) #returns inde of 1st occrence of 'm'
print(str.count("am"))#returns count of "am" in string

#Q- input th last name of user and print its length

lastName = input("enter last name : ")

print("lengthh of last name = ",len(lastName))

#Qfind conut of "a" i a string

string = "electric appliances for sale"
print("no. of a's = ",string.count("a"))

