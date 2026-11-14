def add_all(numbers):
    total = 0
    for n in numbers:
        try:
            total = total + int(n)
        except ValueError:
            print("跳过：", n)
    return total


data = ["10", "abc", "20", "5"]
print(add_all(data))
#这个函数是处理把从列表的值，如果值为int就拉出来的值加到total上。反之则跳过。try+ex...rror兜住错误。
#我认为会返回两行：
# 跳过: abc
# 35
# 顺便一问def add_all():如果这么写，里面会怎么写