def insertion_search(array):
    for i in range(1,len(array)):
        element = array[i]
        j = i-1
        while j >= 0 and element < array[j]:
            array[j+1] = array[j]
            j = j-1
            array[j+1] = element
n = int(input("enter the array elements"))   
array=[]

   