def jiou(number):
    if number % 2 == 0:
        return "偶数"
    else:
        return "奇数"
print(jiou(4)); print(jiou(7))


def dengji(score,pass_line = 60):
    if score >= 90:
        return "优秀"
    elif score >= pass_line:
        return "及格"
    else:
        return "不及格"
print(dengji(95)); print(dengji(72)); print(dengji(40));print(dengji(55,50))