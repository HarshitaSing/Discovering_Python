#d=2 //rotate first 2 elements

arr =[1,2,3,4,5]
arr1 = arr[2:]
for i in range(d):
    arr1.add(arr[i])
print (arr1)
