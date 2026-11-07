# 1.-1是找不到的意思，括号填要找的参数
song = "夜曲_周杰伦_2005.mp3" ; print(song.find("_"),song.find("周杰伦"),song.find("滚木"))
# 2.
pics = ["a.jpg","b.png","c.JPG","d.jpg"]
for p in pics:
    if p.lower().endswith(".jpg"):
        print(p)
# 3.原串没变，括号的两个参数一个是原字符串的，另一个是要替换原字符串的参数
city = "清远→广州→深圳"; print(city); city = city.replace("→", "|") ;print(city);
# 4. 没有改变原字符串
code = "###Eris###"; print(code.strip("#"), code)
# 5.
raw = " Hello_World.TXT "; raw = raw.strip(); raw = raw.lower(); raw = raw.replace("_","-"); raw = raw.endswith(".txt"); print(raw)
# 6.
files = ["note.txt", "photo.jpg"]
for f in files:
    if f.endswith(".txt"):
        print(f)
msg = "I like tea"
msg = msg.replace("tea", "coffee")#没有存回
print(msg)
