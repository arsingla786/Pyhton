#loops are usd to repeat a same task 
#WHILE loop

count = 1
while(count<=5):
    print('hello')
    count=count+1

i=1
while(i<=10):
    print('hi') 
    i+=1


#reverse loop
i=5
while(i>=1):
    print(i , end = ' ') #to print in same line
    i-=1
print('\n''loop end')


# Q print tabbl of a numbebr n 

n= int(input('enter N : '))
i=1 ; 
while(i<=10):
    print( n * i )
    i+=1

#Q-print elements of list using while loop
list = [1,4,9,16,25,36,49,64,81,100]

i = 0
while(i<len(list)):
    print(list[i] ,end = ' ')
    i+=1


#  Q- serach for a number in a tuple
x =  int(input('enter  x : ')) 

tup = (1,4,9,16,25,49,64,81,100)

i=0
exist =0

while(i<len(tup)):
    if(tup[i]==x):
        print("yes it exists at index : ",i)
        break #to xit th loops once found 
    else:
        print("it does not exist ")    
    i+=1


##prit all odd no. btw 1 annd 100

i=1
while(i<=100):
    if(i%2!=0):
        print(i)
    i+=1    