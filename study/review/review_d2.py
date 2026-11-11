names = ["小明", "小红", "小刚", "小丽"]
tels  = ["138000", "139000", "137000", "136000"]
x = "小红"
if x in names:
    i = names.index(x)
    names.pop(i);tels.pop(i)
    for i in range(len(names)):
        print(names[i], tels[i])
print(len(names),len(tels))