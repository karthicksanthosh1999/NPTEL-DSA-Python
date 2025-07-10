arr = [100,40,20,2,5,8,90]

# BUBBLE SORT
def bubbleSort(nums: list):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                 nums[j] , nums[j+1] = nums[j+1], nums[j]
    return nums

result = bubbleSort(arr)
print(result)


