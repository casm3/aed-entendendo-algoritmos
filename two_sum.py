from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    nums = array.data
    vistos = {}

    for i, num in enumerate(nums):
        complemento = target - num

        if complemento in vistos:
            return (vistos[complemento], i)

        vistos[num] = i

    return (-1, -1)