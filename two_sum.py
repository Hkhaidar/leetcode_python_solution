arr=[14,65,7,89,3,4,5,8,]
target=10
arr1=[2,4,5,6,7]
target1=50
def two_sum(arr,target):
    v={}
    
    
    for i , elem in enumerate(arr):
        comp=target-elem
        if comp in v:
            
           return[v[comp],i]
        else:    
            v[elem]=i
    return[]

list1=two_sum(arr,target)
print(list1)

list2=two_sum(arr1,target1)
print(list2)
