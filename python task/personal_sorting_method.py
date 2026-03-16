def get_it_sorted(nums):
    numbers = len(nums)

    for number in range(numbers):
        for index in range(0, numbers - number - 1):
            if nums[] > nums[index + 1]:

                nums[index], nums[index + 1] = nums[index + 1], nums[index]

    return nums

nums = [4, 1, 3, 9, 2]
print(get_it_sorted(nums))
