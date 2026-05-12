from src.my_array import MyArray

def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    vistos = {}
    
    for i in range(len(array)): 
        num_atual = array[i]
        complemento = target - num_atual
        
        if complemento in vistos:
            return (vistos[complemento], i) 
        
        vistos[num_atual] = i 
        
    return (-1, -1)