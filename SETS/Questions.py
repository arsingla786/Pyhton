#Q- put following in a disctionary 

dict = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}

print(dict)

#Q-suppose subjects are given and we require one room for each subject, find no. of rooms

#move all sbjects to a set and print length to get uniques count which is count of rooms
set ={'python','c++','c++','java','python'}
print('no. of rooms neded  =  ',len(set))

#q- input marks of three subject from user and print in form of dictionary us subject  as key
dict = {}
x = int(input("enter physics marks: "))
dict.update({"physics":x})

x = int(input("enter maths marks: "))
dict.update({"maths":x})

x = int(input("enter chem marks: "))
dict.update({"chem":x})

print(dict)


# Q store 9 and 9.0 in a set as different values

set ={9,9.0}
print(set)

#9 , 9.0 are treated same in python

set = {9 , "9.0"}
print(set)  # this is a way or {"9",9.0}




