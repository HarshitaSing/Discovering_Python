#monotonic increasing check in array
arr = [1,2,3,4,5]
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]: # arr[i] > arr[i+1] (monotonic decreasing)
        continue
    else:
        print ("No")
        break
