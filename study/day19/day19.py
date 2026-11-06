nums = [32,42,13,54,95]
print(nums[::])
print(nums[::-1])
print(nums[2:])

nums.sort()
print(nums)

new_nums = sorted(nums)
print(nums, new_nums)
print(len(nums),len(new_nums))

top4 = sorted(nums,reverse=True)[:4]
print(top4)

print([n*2 for n in nums])