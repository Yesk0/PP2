def has_33(nums):
    tf = True
    for i in range(0, len(nums)):
        if i == len(nums):
            break
        elif nums[i] == 3 and nums[i+1] == 3:
            tf = True
            print(True)
            break
        else:
            tf =  False
            continue

nums = [1 ,3 ,3]
has_33(nums)