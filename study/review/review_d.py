# # 1.打印那一行不知道有没有更好的写法
# scores, total, best, count = [78, 92, 55, 63, 88, 95, 71], 0, 0, 0
# for s in scores:
#     total = total + s
#     if s > best:
#         best = s
#     if s >= 60:
#         count = count + 1
# pjf = total / (len(scores))
# print(f"总分：{total}"); print(f"平均分:{pjf}"); print(f"最高分：{best}"); print(f"及格人数：{count}人"); print(f"前三名：{sorted(scores, reverse=True)[:3]}")
# # 2.虽然做出来了，但我这个方法应该是有很大问题的。
# files = ["Report.PDF", "My_note.txt", "photo.JPG", "BACK_UP.TXT", "readme.md"]
# for f in files:
#     f2 = f.lower()
#     if not f2.endswith(".txt"):
#         continue
#     wz = f2.find(".")
#     f3 = f2.replace("_","-")
#     print(f3[:wz])
3.
names, tels = [], []
while True:
    print("请输入数字:1加人 2查号 3删人 q退出")
    choice = input("请输入：")
    if choice == "1":
        xm = input("姓名："); dh = input("电话:")
        names.append(xm)
        tels.append(dh)
        print("已添加", names, tels)
        continue
    elif choice == "2":
        xm = input("姓名：")
        if xm in names:
            xb = names.index(xm)
            print("电话为：", tels[xb])
        else:
            print("查无此人")
        continue
    elif choice == "3":
        xm = input("姓名：")
        if xm in names:
            i = names.index(xm)
            names.pop(i); tels.pop(i)
            print("已删除")
        else:
            print("查无此人")
        continue
    elif choice == "q":
        print("（程序结束，不再出现菜单）")
        break