line=input().split(" ")
n1,n2,n3=line
n1=int(n1)
n2=int(n2)
n3=int(n3)
arr=[n1,n2,n3]
def insertionSort(arr): 
    for i in range(1,3):
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j] 
            j -= 1
            arr[j + 1] = key
insertionSort(arr)             
for i in range(len(arr)):
    print ("%d"%arr[i]) 
print(" ")     
print(n1) 
print(n2)
print(n3)    

    
    
