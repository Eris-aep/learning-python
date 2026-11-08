# 1.continue放在 +1 前面是因为跳过是不计入次数，若+1在前，触发continue的时候会计入
count = 0
while True:
    user1 = int(input("输入数字："))
    if user1 == 99:
        print("跳过且不计次")
        continue
    count = count + 1
    if user1 == 0:
        print(f"有效{count}个数字")
        break   
print()
# 2.检查次数要放在比较之后s是因为循环顺序是从上到下，防止正确答案卡在第四次被吞
answer, count = 30, 0
while True:
    user_a = int(input("猜数字："))
    count = count + 1
    if user_a == answer:
        print(f"答对了,{count}次")
        break
    if user_a > answer:
        print("大了")
    elif user_a < answer:
        print("小了")
    if count >= 5:
        print("次数用完了")
# 3.
count3, m = 0, 0
while True:
    user3 = int(input("输入数字:"))
    if user3 < 0:
        print("此次忽略不计")
        continue
    if user3 == 999:
        print(f"共{count3}个有效数字，其中偶数{m}个")
        break
    count3 = count3 + 1
    if user3 >= 0:
        if user3 % 2 == 0:
            m = m + 1