# 1.最后一步写 raw = raw.endswith(...)会覆盖掉raw，所以应该创建一个新变量
raw = " Report_2026.TXT "; raw = raw.strip(); raw = raw.lower(); raw = raw.replace("2026","2027"); rew = raw.endswith(".txt");print(raw,rew)
# 2.
files = ["note.txt", "photo.jpg", "data.csv"]
for f in files:
    if f.endswith(".txt"):
        print(f)
# 3.replace 本身没改原串存回后 s 这个变量指向replace后的s
s = "abc"; print(s.replace("a","x"), s); s = s.replace("a","x"); print(s); 