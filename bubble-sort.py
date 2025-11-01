def bubble_sort(arr):
    n = len(arr)
    # print(n)
    for i in range(n-1):   
        for j in range(n-i-1):
            # print(i)
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
                 
            
    
arr= [6,0,3,5]
bubble_sort(arr)
print(arr)
        