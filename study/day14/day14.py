Age , gender = input("请输入你的年龄和性别，用空格隔开").split()
Age = int(Age)
if Age >= 18:
    print("成年")
    if gender in["male" , "男" , "man"]:
        print("男性，可进入")
    else:
        print("非男性，不可入内")
else:
    print("未成年")

score = 85
if score > 0 and score > 90:
    print("优秀")
elif score > 90 or score > 75:
    print("良好")
elif score >= 60:
    print("及格")
if not score >= 60:
    print("不及格")

filename = "Eris.aep"
if filename.endswith(".aep") and len(filename) > 4:
    print("此文件为合格的aep后缀文件")
else:
    print("不是后缀为.aep的文件")