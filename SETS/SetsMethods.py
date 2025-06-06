nums = {1,2,3,3,4,5,6,7,7}

print(nums)

nums.add(0)
nums.add(10) #adds a new value

nums.remove(1)
nums.remove(3) #removes all occurnces 

print(nums)
print(len(nums))

nums.pop()
print(nums)   #pops a random value


nums.clear()
print(len(nums)) #clears the set 


set1={1,2,3}
set2={2,3,4,5}

print(set1.union(set2)) #prints combined two sets

print(set1.intersection(set2)) #prints common elements between two sets



