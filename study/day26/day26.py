import os
print(os.listdir("study/day26/files"))


import datetime
date = datetime.datetime.now().strftime("%Y%m%d")
print(date)


names = os.listdir("study/day26/files")

for name in names:
    mulu = "study/day26/files"
    old = mulu + "/" + name
    new = mulu + "/" + date + "_" + name
    os.rename(old,new)
    print(name,"->",date + "_" + name)
print(os.listdir("study/day26/files"))