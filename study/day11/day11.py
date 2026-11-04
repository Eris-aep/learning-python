s = "Eris_aep.com"
print(s.find("aep"))
print(s.find("123"))

print(s.replace("com","@qq.com"))

a = "鲁迪|Eris|Roxy"
print(a.split("|"))
print(a.startswith("鲁迪"))
print(a.endswith("鲁迪"))

Name , City , Age = "Eris" , "魔大陆" , "21"
print(f"你好！我叫{Name},来自{City},今年{Age}岁！")