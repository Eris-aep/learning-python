 # 1.
shopping = ["牛奶","鸡蛋","面包"];
# print(len(shopping))
# 2.我忘了咋写了
shopping.
# 3.应该有更好的写法
shopping.append("你好");print(shopping)
shopping.append("鹅蛋");print(shopping)
shopping.remove("面包");print(shopping)
shopping.pop(0);print(shopping)
input(shopping.pop());print(shopping)
# 4.
for s in shopping:
    print(f"要买:{s}")
# 5.
nums = [5,2,9,1,7,3,8];print(nums[:3],nums[-3:],nums[1:4],nums[::-1])
# 6. 按照如下写法原列表自然是被改变了。但 其他 == nums.sort()则打印nums时不会改变原列表
nums == nums.sort(); print(nums)
# 7.我乱做的,没懂
sorted(nums, reverse=True);print(nums[:3],nums)
8.不会，也没听懂题

