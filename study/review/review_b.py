# 1.负数的我不会
User_text = int(input("请输入你的年龄:"))
if User_text >= 18:
    print("成年")
elif User_text <= 18:
    print("未成年")
elif User_text <= 0:
    print("无效")
# 2.
User_text_2 = int(input("请输入你的成绩:"))
if User_text_2 >= 90:
    print("优秀")
elif User_text_2 >= 75:
    print("良好")
elif User_text_2 >= 60:
    print("及格")
else:
    print("不及格")
# 3.not的我不会
has_id, age = True, 20; User_age,User_card = int(input("你的年龄")), input("卡名：");
if age == 20 and has_id == True:
    print("通过")
elif age == 20 or has_id == True:
    print("通过")
elif age == 20 not has_id == True:
# 4. 也做不完整。
Age_4,card_4 = int(input("请输入你的年龄：")), True;card_User = input("有没有带证：");
if Age_4 >= 18:
    print("成年")
    if card_4 == card_User:
        print("带证")
    elif card_4 != card_User:
        print("没带证")
else:
    print("未成年")
# 5. 可能我没听懂你的意思？我不知道你是不是让我这样做
print(range(5));print(range(1,6));print(range(0,11,2));
# 6.
print()
# 7.完了总感觉只差一点疑意思
list = ["a.txt","b.jpg","c.txt"];
for l in list:
    print(l)
    l = l + l
# 8.也不完全会啊
user_8, daan = int(input("猜数字:")), 19;
for u_8 in user_8:
    if u_8 == daan:
        print("猜对了")
        break
    elif u_8 > daan:
        print("猜大了")
    elif u_8 > daan:
        print("猜小了")