# # 1.如果不接住，用什么方法改变对象最后打印s都是原列表
# s = " Hello "; x = s.strip(); print(x, len(x))
# # 2.不会
# msg = "I like tea";msg = msg.endswith("tea","coffee"); print(msg)
# # 3.
# items = ["红","蓝","绿"]; print(len(items),items[0],items[-1],items.index("蓝")); print(items); items[2] = "黄"; print(items)
# # 4.
# items.append("紫"); print(items);
# items.append("白"); print(items);
# items.remove("红"); print(items);
# X = items.pop(); print(X)
# items.pop(0); print(items)
# # 5.原列表改了,sort返回排序好的nums
# nums = [12,3,8,20,1]; nums.sort(); print(nums)
# # 6.
# x6 = sorted(nums, reverse=True)[:3]; print(x6,nums,nums[::-1])
# # 7.
# a = [n*2 for n in nums]; b = []
# for n in nums:
#     b.append(n * 2)
# print(a,b, a==b)