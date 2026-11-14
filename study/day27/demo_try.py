print("情况1：输入abc(不是数字)")
shi = "abc"
count = 0
try:
    n = int(shi)
    print("转换成功:n=:",n)
except ValueError:
    print("你输入的不是数字")
print("程序活到了这里")

print("===情况1：输入abc(不是数字)===")
s = 42
try:
    j = int(s)
    print("转换成功：j=:",j)
except ValueError:
    print("你输入的不是数字")
    print("程序活到了这里")

#L2
print("===情况1: 第三次才输对===")
shuru = ["1111", "2222", "1234"]
mima = "1234"; count = 0
while count < 3:
    shu = shuru[count]
    print("用户输入:",shu)
    if shu == mima:
        print("答对了")
        break
    count = count + 1
    print("答错,还剩",3-count,"次")
if count == 3:
    print("没机会了")


print("===情况2: 三次全错===")
shuru = ["1111", "2222", "3333"]
mima = "1234"; count = 0
while count < 3:
    shu = shuru[count]
    print("用户输入:",shu)
    if shu == mima:
        print("答对了")
        break
    count = count + 1
    print("答错,还剩",3-count,"次")
if count == 3:
    print("没机会了")
