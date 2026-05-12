from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    
    if len(array) <= 1:
        return array 
    
    pivot = array[0]
    idx_arr = len(array) - 1
    
    i = 0
    j = idx_arr
        
    while i < j :
        while i < j and array[i] <= pivot:
            i += 1
                
        while i < j and array[j] > pivot:   
            j -= 1
        
        array[i], array[j] = array[j], array[i]
        
    array[0], array[j] = array[j], array[0] 
    
    left_array = array[:j]
    right_array = array[j+1:]
    
    quick_sort(left_array)
    quick_sort(right_array)
        
    return array