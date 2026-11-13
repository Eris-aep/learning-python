with open("study/day25/note.txt","w",encoding="utf-8") as f:
    f.write("第一行\n"); f.write("第二行\n"); f.write("第三行\n")


with open("study/day25/note.txt","a",encoding="utf-8") as f:
    f.write("第四行\n")


with open("study/day25/note.txt","r",encoding="utf-8") as f:
    for lines in f.readlines():
        print(lines.strip())
    
