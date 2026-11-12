students = [{"姓名":"Eris","分数":78},{"姓名":"Rudy","分数":91}
            ,{"姓名":"Roxy","分数":69},]
count = 0; grade = 0
for s in students:
    count = count + int(s["分数"])
    print(f"{s['姓名']}: {s['分数']}")
    if s["分数"] > grade:
        grade = int(s["分数"])
print("总分:",count)
print("最高分:",grade)