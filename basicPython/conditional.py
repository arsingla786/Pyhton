# age = int(input('enter age : '))

# if(age>=18):
#     print('can drive')

# elif(age>=30):
#     print('can drive truck')

# else:
#     print('cannot drive')

# Input the color and give traffic signal
light = input('light : ')

if(light=='Red'):
    print('stop')
elif(light=='Yellow'):
    print("look")
elif(light=="green"):
    print("Go")
else:
    print("Light is malfunction")            

#Input marks and print grade
marks = int(input("marks : "))
if(marks>=90):
    print('A')    
elif(marks>=80 and marks<90):
    print('B')
elif(marks>=60 and marks<80):
    print('C')
else:
    print('FFail')     

#Ternary operator - check conditions in a single line
food = input("food : ")
eat = 'Yes' if food=="cake" else 'no'
print(eat)    

print("sweet") if food == 'cake' or food=="jalebi" else print('not sweet')

# clever if else

salary =int(input('salary : '))

tax= salary*(0.1,0.2) [salary>=50000]   #0.1 if false , 0.2 if true
print(tax)