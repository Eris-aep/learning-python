# 1. strip()是去除字符串两头的空格，如果括号内有其他符号则去除其他。split()则是设置分隔符，默认是空格
raw = " Eris "; print(raw.strip(), raw.split())
# 2.
X = "18"; X = int(X) + 2; X = str(X); print("年龄：" + X)
# 3.
name = " eris ";print(name.strip(), len(name), name.strip()[0], name.strip()[-1])
# 4. 第一个去空格、二全大写、三全小写、四原字符串
s = " Hello Python "; print(s.strip(), s.upper(), s.lower(), s)
# 5. -1是不存在的意思 其他的我不会了，我知道这个
# t = "report_2026.txt";print(t.find())
# 6.
msg = "I like tea"; print(msg.replace("tea","coffee"), msg); msg_new = msg.replace("tea","coffee"); print(msg_new)
# 7.不会做
# files = ["note.txt","photo.JPG","data.csv","备忘录.TXT"];
# for f in files:
#     f = files.endswith(.txt)
# 8.end的默认值是换行符
T = "你好"; print(T,end=""); print(T)
# 9. 当bool("")留空、0、None时是false，当""有参数时，正确答案即本身，所以永远true。正确写法是 X = True
print(bool(""), bool("魔大陆"), bool(0), bool(1), bool("False"))
# 10 剩下的不会了
# raw_10 = " Report_2026.TXT "; print(raw_10.strip(), raw_10.lower(), raw_10.replace("2026","2027"), raw_10.endswith())