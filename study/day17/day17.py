i = 1
while i<=5:
    print(i)
    i = i+1

key , count = 9 , 0
while True:
    User_key = int(input("输入1~10其中一个数字:"))
    count  = count + 1
    if User_key == key:
        print("你答对了！")
        break
    elif User_key >= key:
        print("猜大了，小一点")
    else:
        print("猜小了，大一点")
    if count >= 5:
        print("没机会了")
        break