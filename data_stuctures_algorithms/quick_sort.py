def partition(arr,low,high):
    below=low-1
    for i in range(low,high):
        if arr[i]<=arr[high]:
            below+=1
            arr[below],arr[i]=arr[i],arr[below]
    arr[high],arr[below+1]=arr[below+1],arr[high]
    print(arr)
    return below+1


def qui_sort(arr,low,high):
    if low<high:    
        pi=partition(arr,low,high)

        qui_sort(arr,low,pi-1)
        qui_sort(arr,pi+1,high)

if __name__=="__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    print('initial array')
    print(arr)
    qui_sort(arr,0,n-1)
    print('final array')
    print(arr)
