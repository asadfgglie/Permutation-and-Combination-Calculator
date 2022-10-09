from . import C

def H(n, r):
    if n < 1:
        return 0
    elif r < 1:
        return 0
    
    return C.C(n + r - 1, r)

def main():
    while (True):
        inp = input("Input '/stop' or 'H': ")
        if inp == '/stop':
            exit()
        elif inp == "H" or inp == 'h':
            try:
                n = int(input("Input n: "))
                r = int(input("Input r: "))
                num = H(n, r)
                if num == 0:
                    print("The input numbers are wrong.")
                else:
                    print(f"H({n}, {r}) = {num}")
            except:
                print("Please input the number.")
        else:
            print("Please input the command.")

if __name__ == '__main__':
    main()