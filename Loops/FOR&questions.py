#for loops 

list = [1,2,3,4,5]

for num in list:
    print(num)


#Q- find a char in string

string="anonymous"    

for char in string:
    if(char=='o'):
        print('found',char)
        break #to exit the loop
    else:
        print(char)


#RANGE function   range(start , stop , step size )
#start = 0 by default , step = 1 bby  default

for el in range(5):
    print(el)  # 0 1 2 3 4 

for el in range(1,5):
    print(el)     # 1 2 3 4 

for el in  range (1,5,2):
    print(el)  #1 3

#print even no. in 0 to 100

for el in range(0,101,2):
    print(el,end= ' ')


#print no. from 100 to 1
for el in range(100,0,-1):
    print(el)    


#pint tabbl of n
n= int(input("entr n : "))

for i in range(1,11,1):
    print(i*n,end=' ')

#print sum of n natural no.
n=int(input("enter n : "))
print('\n')
sum=0
for i in range(0,n+1):
    sum+=i

print(sum)





