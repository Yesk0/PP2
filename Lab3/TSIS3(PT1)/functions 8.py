def spy_game(nums):
    tf = False
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            tf = True
            print(True)
            break
    else:
        print(False)

nums = [1, 3, 3, 0, 0, 7, 1]
spy_game(nums)

