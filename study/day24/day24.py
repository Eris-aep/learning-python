with open("study/day24/demo.txt","r",encoding="utf-8") as f:
    lines = f.readlines()

for l in range(len(lines)):
    print(f"{l + 1}.{lines[l].strip()}")