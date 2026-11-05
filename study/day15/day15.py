Chinese , English = map(int,input("语英多少分").split())
print(f"语文 {Chinese} , 英语 {English} ,")

op = input("只可输入 (+ - *) :")

if op == "+" :
    print(Chinese + English)
elif op == "-" :
    print(Chinese - English)
else:
    print(Chinese * English)

print(f"{Chinese} + {English} = {Chinese+English}")

