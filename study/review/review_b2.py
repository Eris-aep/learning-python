# 1.
bodytemperature = float(input("输入你的体温："))
if bodytemperature > 50 or bodytemperature < 0:
    print("无效")
elif bodytemperature >= 37.3:
    print("发烧")
else:
    print("正常")
# 2.
money = int(input("输入金额："))
if money >= 1000:
    money = money * 0.8
    print(money)
elif money >= 500:
    money = money * 0.9
    print(money)
elif money >= 100:
    money = money * 0.95
    print(money)
# 3.我实在看不明白你的意思
is_vip, score = False, 85;
# 4.
age,card = int(input("年龄：")), input("有没有带学生证(有/无):");
if age >= 18:
    print("已成年")
elif age < 18:
    if card == "无":
        print("未带证")
    else:
        print("可购买")
# 5.第一个是打印下标0～5的数，应该是叫下标。第二个左闭右开。第三个一样，但每拉取一位数，间隔两步
print(list(range(5)));print(list(range(3,7)));print(list(range(0,101,2)))
# 6.
y_range, count = list(range(3,50,3)), 0; print(y_range)
for y in y_range:
    count = count + 1
    print(y)
print(count)
# 7.累加器放进循环里是为了每次拉取再次计数，拉取结束之后正好统计完了
s, count_7 = ["a.log","b.txt","c.log","d.txt"], 0;
for S in s:
    count_7 = count_7 + 1
    print(S)
print(f"{count_7}个")
# 8.
daan = 42; count_8 = 0
while True:
    User_text = int(input("请你输入答案："))
    if daan < 0:
        print("本次不算，重来")
        continue
    count_8 = count_8 + 1
    if User_text == daan:
        print("你答对了!")
        break
    elif User_text > daan:
        print("你猜大了")
    else:
        print("你猜小了")
    if count_8 > 6:
        print("次数用完了")
        break
# 9.
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{i} X {j} = {i*j}", end="\t")
    print()
