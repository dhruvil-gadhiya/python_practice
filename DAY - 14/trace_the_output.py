# Given a short Python code snippet (e.g., involving loops, slicing, or list comprehensions), explain step-by-step what the output will be...

nums = [10, 20, 30, 40, 50, 60]

# slicing with step
part1 = nums[1:5:2]      

# negative indices and reverse step
part2 = nums[-2:0:-2]    

# list comprehension with condition
comp = [x//10 for x in nums if x % 20 == 0]

print(part1)
print(part2)
print(comp)



