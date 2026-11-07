# 1.（包括2.，因为我认为我没理解的错话,2.的目的1.已经达到，如若没达到叫我补就行
Age, height, name, address = 18, 1.75, "Eris", bool("魔大陆")
print(type(Age),type(height),type(name),type(address));print(Age, height, name, address)
# 3.
A = int(input("请你输入第一个数：")); B = int(input("第二个数"))
print("两者和为：",A + B, "两者差为:", A - B, "两者乘为：", A * B, "两者商为：", A / B, "两者整除：", A // B, "两者除于：", A % B, "两者次方：", A ** B)
# 4.
X = int(18);print(X + 2); X = str(X); print("年龄：" + X)
# 5.
print(10/2, 10//3, 10%3, 2**10, int(3.14)) #int() 是截断不是四舍五入。
# 6.
a, b= 17,5; print(a > b, a >= b, a == 17, a != b, a <= b, a%2 == 0)
# 7.
name_7, city, age_7 = "Eris", "迷宫", 18; print(f"我叫{name_7},住在{city},今年{age_7},两年后{age_7 + 2}")
# 8.
name_8 = input("你的名字");print(name_8.split(), len(name_8), name_8[0], name_8[-1])
# 9.
address_9 = "狗镇，太平州，海伍德，动物帮"; print(len(address_9), address_9[0], address_9[-1], address_9[1:4], address_9[:3], address_9[3:], address_9[::-1])
# 10.
# s = " Hello Python"; print(s.split(), s.startswith(), s.endswith()) 不会写后面两个
# 11.
# text = input("输入大小写英文+中文"); print(text.find(),text.replace(), text.split(), text.startswith(), text.endswith()) 不明白除了split的其他意义
# 12
print("A","B","C", sep="-"); print("A","B","C", end="") #sep是更改间隔号,""空着默认空格间隔，有符号默认用此符号间隔。end是输出后禁止进行任何操作