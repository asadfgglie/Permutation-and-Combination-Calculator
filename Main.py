from function import H
from function import C
from function import P
from function.Factorial import factorial as F

import os

command = ""

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platform
        _ = os.system('cls')
    # print out some text
    print("輸入'C', 'H', 'P', 'F'來計算數值(不分大小寫)\n輸入'/stop'關閉程式(分大小寫)\n輸入'[指令] -h'查詢指令細節\n輸入'/clear'清除螢幕(分大小寫)")

def main():
    global command
    print("輸入'C', 'H', 'P', 'F'來計算數值(不分大小寫)\n輸入'/stop'關閉程式(分大小寫)\n輸入'[指令] -h'查詢指令細節\n輸入'/clear'清除螢幕(分大小寫)")
    while True:
        try:
            command = input("> ")
        except KeyboardInterrupt:
            exit()

        if command == '/clear':
            screen_clear()

        elif command == 'C' or command == 'c':
            n = int(input("輸入n:> "))
            r = int(input("輸入r:> "))
            result = C.C(n, r)
            print(f"C({n}, {r}) = {result}")
        elif command == 'H' or command == 'h':
            n = int(input("輸入n:> "))
            r = int(input("輸入r:> "))
            result = H.H(n, r)
            print(f"H({n}, {r}) = {result}")
        elif command == 'P' or command == 'p':
            n = int(input("輸入n:> "))
            r = int(input("輸入r:> "))
            result = P.P(n, r)
            print(f"P({n}, {r}) = {result}")
        elif command == 'F' or command == 'f':
            n = int(input("輸入數字:> "))
            result = F(n)
            print(f"{n}! = {result}")
        elif command == '/stop':
            exit()
        
        elif command == 'H -h' or command == 'h -h':
            print("H(n, r): 從n種物品中任取r個物品，共有H(n, r)種取法")
            print("例如: 有x, y, z三種物品，求: x + y + z = 10的非負整數解數量")
            print("答: H(3, 10)")
            print("請依序輸入'H'、'3'、'10'求得H(3, 10)之值")
        elif command == 'P -h' or command == 'p -h':
            print("P(n, r): 從n個相異物品中任取r個並排列，共有P(n, r)個排列")
            print("例如: x, y, z三個物品，求任取2個並排列的可能排法")
            print("答: P(3, 2)")
            print("請依序輸入'P'、'3'、'2'求得P(3, 2)之值")
        elif command == 'F -h' or command == 'f -h':
            print("F為階乘計算工具")
            print("請依序輸入'F'、'5'求得5!之值")
        elif command == 'C -h' or command == 'c -h':
            print("C(n, r): 從n個相異物品中任取r個並\"不\"排列，共有C(n, r)個取法")
            print("例如: x, y, z三個物品，求任取2個的可能取法")
            print("答: C(3, 2)")
            print("請依序輸入'C'、'3'、'2'求得C(3, 2)之值")

        else:
            print("請輸入正確指令")
            print("輸入'C', 'H', 'P', 'F'來計算數值(不分大小寫)\n輸入'/stop'關閉程式(分大小寫)\n輸入'[指令] -h'查詢指令細節\n輸入'/clear'清除螢幕(分大小寫)")

if __name__ == "__main__":
    main()