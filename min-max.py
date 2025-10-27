arr = [0.1,1,2,3,4,5,6]

max_num = arr[0]
min_num = arr[0]
for numbers in arr:
    
    if numbers > max_num:
        max_num = numbers
    elif numbers < min_num:
        min_num = numbers 
        
print(max_num)
print(min_num)
