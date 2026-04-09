def twoSum(nums, target):
    lookup = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in lookup:
            return lookup[complement], i

        lookup[nums[i]] = i

    return -1, -1


# 🔹 Taking dynamic input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))
target = int(input("Enter target: "))

index1, index2 = twoSum(nums, target)

if index1 != -1:
    print("Indices:", index1, index2)
    print("Values:", nums[index1], nums[index2])
else:
    print("No pair found")