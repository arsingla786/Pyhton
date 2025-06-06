#it is a data type in which info is stored in key:value format 

info = {
    "name":"arun",
    "class" : "10th",
    "rollno":9,
    "marks" : 95.5,
    "gender" : 'M',
    "subjects" : ['python','C/C++','Java']
}

print(info)

'''can store any data like string ,int,float , list,tuples in values 
but keys cant be list and tuples'''

teacher = {
    "subjects" : ('database','maths','english','programming'),
    "departements":('civil','mechanical','COE','Electrical'),
    "salary":[20000,10000,30000,45000]
}

print(teacher)

print(info['name']) #can access any key through this format

print(teacher['departements']) #only prints departements

#to change values 
info['class']="9th"
info['gender']="F"
print(info)

#to add any new key and value
info['surname']="yadav"
print(info)

#we can create an empty dictionary

empty_info = {}

print(empty_info)

empty_info["name"] = "araav",'aa'

print(empty_info)
