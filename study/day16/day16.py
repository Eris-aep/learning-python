image , name = ["Rudy.png","Roex.jpg","Sylphy.jpeg"] , ["Eris", "Roxy", "Rudy", "Sylphy"]
for i in image:
    print("处理：" + i)

for i in range(1,6):
    print(i)

for i in name:
    print(i)

for s in range(2,101,2):
    print(s)

for ss in range(1,101):
    if ss % 2 ==0:
        print(ss)

# 以下是挑战
for l in range(1,10):
    for j in range(1,10):
        print(f"{l} x {j} = {l*j}")
# 以下是我打完上面后绝对输出的不够标准后去查ai之后凭记忆打的：
for l in range(1,10):
    for j in range(1,l + 1):
        print(f"{l} x {j} = {l*j}",end = "\t")
    print()
