# 1.要两个都是对的才是真所以true、翻转真假、其中一个对就是真但由于flag是假所以输出false
a, b, flag = 10, 0, False;print(a>b and flag, not flag, a<b or flag)
# 2.else不能省的原因是如果省的花输入小于60的数则不会做任何输出
user2 = int(input("输入分数0-100:"))
if user2 < 0 or user2 > 100:
    print("无效")
elif user2 >= 90:
    print("优秀")
elif user2 >= 60:
    print("及格")
else:
    print("不及格")
# 3.continue是跳回到whili的循环，break是退出当前循环
count = 0
while True:
    user3 = input("输入数字：")
    count = count + 1
    if user3 == 0:  
        print("此次不算，重来不计入次数")
        continue
    if user3 == -1:
        break
    print(f"一共累计{count}个数字")
# 4.
answer,count_4 = 42, 0
while True:
    User4 = int(input("输入数字："))
    count_4 = count_4 + 1
    if count_4 >= 5:
        print("猜不中")
        break
    if User4 > answer:
        print("猜大了")
    elif User4 < answer:
        print("猜小了")
    else:
        print("猜对了")
        break
# 5.
age = int(input("输入年龄"))
if age >= 18:
    print("已成年") ;ticket = input("是否有票（有/无）？")
    if ticket == "有":
        print("成年有票,可进入")
    elif ticket == "无":
        print("成年无票，不可入内")
if age < 18:
    print("未成年,禁止入场")
