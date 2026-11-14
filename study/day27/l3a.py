wenben = "abc"
try:
    n = int(wenbenn)
    print("转换成功", n)
except ValueError:
    print("接住了 ValueError")


# B比A危险是因为B无条件的把所有报错都接住了，难通过跑代码的报错反找出错误点