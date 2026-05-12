from src.my_array import MyArray

def quick_sort(array: MyArray) -> MyArray:
    _quick_sort_logic(array, 0, len(array) - 1)
    return array

def _quick_sort_logic(numbers: MyArray, start: int, end: int):
    if start < end:
        pivot = numbers[end] 
        delimiter = start - 1
        
        for index in range(start, end):
            if numbers[index] <= pivot:
                delimiter += 1
                numbers[delimiter], numbers[index] = numbers[index], numbers[delimiter]
        
        numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]
        
        pivot_index = delimiter + 1
        
        _quick_sort_logic(numbers, start, pivot_index - 1)
        _quick_sort_logic(numbers, pivot_index + 1, end)