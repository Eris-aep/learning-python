name = ["Rudy","eris","Roxy","Sylphy"]
print(name[0], name[-1])
print(len(name[-1]))
print("Rudy" in name)

name [1] = "Eris"
name.append("无职转生")
name.remove("Rudy")
name_x = name.pop()
name_y = name.pop(2)
print(len(name))

for goumai in name:
    print("要买：" + goumai)

while True:
    User_answer = input("请你输入要加入的名字：")
    if User_answer == "q":
        print("成功退出")
        break
    else:
        name.append(User_answer)
        print(name)
        print("添加成功")
