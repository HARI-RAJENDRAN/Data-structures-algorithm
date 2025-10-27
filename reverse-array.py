#reverse array 
arr = [1,2,3,4,5,6]
rev = []
length = len(arr)
# print(length)
for i in range (length):
    # print(i)
    add = rev.append(arr[length-1-i])
    
print(rev)
    
    
