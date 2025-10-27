arr = [10,20,30,40,50,60,20,100]
target = 100
for i in range(len(arr)):
    if target == arr[i]:
        print(arr[i])
    else:
        i +=1 
        