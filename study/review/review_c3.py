# 1.原串没变,replace 两个参数前者为原字符串的某串字符，后者则是用来替换前者的
t = "Day19 复习";t2 = t.replace("19","20"); print(t2,t)
# 2.两个方法前者判断某元素是否在变量里，后者查询某元素在变量中的位置（如果没有元素会报错）、查询内容用in，查询已确定内容下标用index
words = ["红","蓝","绿"]; print("黄" in words,words.index("绿"))
# 3.sort改原件、sorted返回新件、sort() 返回none
nums = [9,4,7,1]; print(sorted(nums),nums)
f = nums.sort(); print(f,nums)
# 4.
nums4 = [9, 4, 7, 1, 8, 3]; print(nums4); print(sorted(nums4,reverse=True)[:3])
x4 = nums4.sort(); print(x4); print(nums4)
5.
s5 = "Day19 复习 Day19";news5 = s5.replace("19","20"); words5 = ["红", "蓝", "绿", "蓝"]; print(news5, s5)
print("黄" in words5,words5.index("蓝"))