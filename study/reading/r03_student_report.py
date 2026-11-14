def report(numbers):
    total = 0
    count = 0
    for n in numbers: 
        try:
            total = total + int(n)
            count = count + 1
        except ValueError:
            print("跳过：",n)
    print("有效数据", count, "条")
    print("平均分", total / count)


data = ["90", "80", "abc", "100"]
report(data)

#2.要把被函数调用的列表里的值遍历然后输出统计有效数据次数 和 值平均分
# 3.第五行：放在了try外面，导致无效数据被统计。第九行（这里八行应该没必要改。且你的输出只是跳过，没有要求说明自然不需要ValueError)。
# except内是pass。pass是直接跳过不做任何，导致了根本不知道错误是什么且不知道有错误
# 4.修好了
# 5.
# print(int(None)) 错误值：TypeError。意思是int的对象必须是像str()、int()、float()这种。而不是None这种空值