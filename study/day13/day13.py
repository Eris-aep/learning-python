Age , score , X , Y = int(input("你几岁？")) , int(input("你语文几分？")) , 20 , 7
if Age >= 18:
    print("成年了")
else:
    print("未成年")

if score >= 85:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

if X > Y and X - Y > 0:
    print("X比Y大")
else:
    print("X比Y小")

if X < Y or X - Y > 0:
    print("X比Y大")
else:
    print("X比Y小")

if X > Y and X - Y < 0:
    print("X比Y大")
else:
    print("X比Y小")

if X > Y and score > 99:
    print("X比Y大")
if not score > 99:
    print("X比Y小")