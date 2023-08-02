###This directory contains dsa questions and their answers
____
Question 1:

    Given an array nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
    
Solution 1:

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

Explanation :

    At this point I only know the basics so the time complexity of my solution is O(n^2). Which is not efficient when the given array is a larger one.