# d = {"小明": "138000", "小红": "139000", "小刚": "137000"}
# print(d["小明"]); print(d.get("小丽", "查无此人"))
# d["小丽"] = "136000"; d["小刚"] = "137111"; print(d)
# for k in d:
#     print(k,d[k])
l_b = {}
while True:
    print("1 加人","2 查号","3 删人","q 退出")
    x = input("请输入:")
    if x == "1":                    #输入1  完工
        xm = input("姓名：")
        dh = input("电话:")
        l_b[xm] = dh
        print("已添加")
    elif x == "2":                  #输入2  完工
        ch = input("姓名：")
        if ch in l_b:
            print("电话号：", l_b.get(ch, "查无此人"))
        else:
            print("查无此人")
    elif x == "3":                  #输入3 完工
        sc = input("姓名：")
        if sc in l_b:
            l_b.pop(sc)
            print("已删除")
        else:
            print("查无此人")
    elif x == "q":                  #输入q  完工
        print("退出查询")
        break

    