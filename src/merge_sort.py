from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    
    tam_array = len(array)
    
    if tam_array <= 1:
        return array      
    
    meio = tam_array // 2
    
    esq_array = MyArray()
    
    for i in range (meio):
        esq_array.insert(i, array[i])        
    
    dir_array = MyArray()
    
    for i in range (meio, tam_array):
        dir_array.insert(i - meio, array[i])
    
    
    esq_array = merge_sort(esq_array)
    dir_array = merge_sort(dir_array)
    
    #merge
    array_mesc = MyArray()

    i = 0 #pont esq
    j = 0 #pont dir
    k = 0 #pont central
    while i < len(esq_array) and j < len(dir_array) :
        if esq_array[i] <= dir_array[j]:
            array_mesc.insert(k, esq_array[i])
            i += 1
        else: 
            array_mesc.insert(k, dir_array[j])
            j += 1 
        k +=1
        
    while i < len(esq_array):
        array_mesc.insert(k, esq_array[i])
        i += 1
        k +=1
    
    while j < len(dir_array):
        array_mesc.insert(k, dir_array[j])
        j += 1 
        k +=1
    
    return array_mesc
    