# 文件：r01_score_report.py
# 作用：把一段成绩单文本整理成一份汇总报告
# 数据格式：每行「姓名,语文,数学,英语」，逗号分隔

RAW = """小明,80,90,70
小红,95,88,92
小刚,60,75,80
小丽,100,99,98""" 
# print(RAW)

def parse_line(line):          
    # 用逗号把一行切成 4 段
    parts = line.split(",")    
    name = parts[0]           
    scores = parts[1:]          
    return name, scores      


def total_of(scores):
    # 把这一行的三个分数加起来
    total = 0
    for s in scores:
        total = total + int(s)
    return total


def build_report():
    # 逐行处理，把姓名和总分分别装进两个列表
    names = []
    totals = []
    for line in RAW.split("\n"):
        if line.strip() == "":
            continue
        name, scores = parse_line(line)
        names.append(name)
        totals.append(total_of(scores))
    return names, totals


def find_best(totals):
    # 打擂台找最高分
    best = 0
    for t in totals:
        if t > best:
            best = t
    return best


def main():
    names, totals = build_report()
    for i in range(len(names)):
        print(names[i], totals[i])
    print("最高分", find_best(totals))


main()