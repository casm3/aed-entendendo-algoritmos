from src.my_array import MyArray


def two_sum(nums, target):
    size = len(nums)

    for i in range(size):
        for j in range(i + 1, size):
            if nums[i] + nums[j] == target:
                return (i, j)

    return (-1, -1)