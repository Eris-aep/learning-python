# 包含L2
count = 0
while count < 3:
    try:
        User_1,User_2 = int(input("请你输入的一个数:")), int(input("第二个数"))
        he = User_2 + User_1
        print(he)
        break
    except ValueError:
        print("你输入的不是数字,请重新运行")
    count = count + 1
    print("还剩下",3-count,"次")
if count == 3:
    print("三次都错了，程序退出")