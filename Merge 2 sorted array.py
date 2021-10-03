#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def merge_2_array(arr,brr):                          #Declaring a function
    li=[]                                            #Creating a list which will contain the sorted element of both sorted array
    i=0                                              #A variable that will go from 0 to (length of list - 1)
    j=0
    while i<=(len(arr)-1) and j<=(len(brr)-1):       #As we know that indexing can never be greater than the lenth of list so these condition
        if arr[i]<brr[j]:                            #Comparrision between the elemente of two different element in two different list
            li.append(arr[i])                        #Apeending the smaller element in the empty list that we created
            i=i+1                                    #Incrementing
        elif arr[i]>=brr[j]:                         #Again comparing and appending the smaller element in the list 
            li.append(brr[j])
            j=j+1                                    #incrementing the list
    if len(arr)>len(brr):                            #if the length of any of the list is greater than the other one then extending the elements of the longer list to the list that we created 
        li.extend(arr[len(brr):])
    else:
        li.extend(brr[len(arr):])
    return li
arr=[int(x) for x in input().split()]                #List comprehension for taking the input of the lists
brr=[int(x) for x in input().split()]
arr.sort()                                           #sorting the individual array
brr.sort()  
res=merge_2_array(arr,brr)                           #Calling the function that we created and storing the refferencing of final list to the variable called res 
print(res)                                           #Printing the result

