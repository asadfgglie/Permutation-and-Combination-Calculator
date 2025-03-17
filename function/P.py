def P(n, r):
    sum = 1
    if r < 0 or r > n:
        return 0

    for i in range(n, n - r, -1):
        sum *= i
    return sum

def main():
    while True:
        inp = input("Input '/stop' or 'P': ")
        if inp == '/stop':
            exit()
        elif inp == "P" or inp == 'p':
            try:
                n = int(input("Input n: "))
                r = int(input("Input r: "))
                num = P(n, r)
                if num == 0:
                    print("The input numbers are wrong.")
                else:
                    print(f"P({n}, {r}) = {num}")
            except:
                print("Please input the number.")
        else:
            print("Please input the command.")

if __name__ == '__main__':
    main()