dict = {
    "name":"aman",
    "class":"12th",
    "rollno":"34",
    "subjects": ['maths','physics','english'],
    "marks":{
        "maths":47,
        "physics":45,
        "english":43
    }

}


print(list(dict.keys()))  #to print list of all keys

print(len(dict)) #gives no. of keys
 
print(dict.values()) #prints all the values present in dictionary

print(list(dict.values()))

print(dict.items()) #rturns all th key : valus pairs in a form of tuples

# pairs = list(dict.items())
# print(pairs[0])

print(dict.get("name")) #eturn values according to the key #return none when given wrong key name
print(dict["name"])  #return error when given a wrong key name

#these both have same output
dict.update({"name":"abhi",'age':16}) #to make changes in dictionary or add new keys:values
print(dict)


