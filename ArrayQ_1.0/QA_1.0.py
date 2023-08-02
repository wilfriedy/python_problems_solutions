def findTarget (array_of_nums, target):
    if len(array_of_nums) == 0:
        return
    for i in range(len(array_of_nums)):
        for j in range(i+1, len(array_of_nums)):
            if array_of_nums[i] + array_of_nums[j] == target:
                return [i,j]
    return  []


nums = [2, 7, 11, 15]
target = 9
result = findTarget(nums, target)
print(result)