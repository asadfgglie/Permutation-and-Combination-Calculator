from . import P
from . import Factorial

def C(n, r):
    if r < 0 or r > n:
        return 0

    if r > n / 2:
        r = n - r

    return P.P(n, r) // Factorial.factorial(r)

def main():
    while (True):
        inp = input("Input '/stop' or 'C': ")
        if inp == '/stop':
            exit()
        elif inp == "C" or inp == 'c':
            try:
                n = int(input("Input n: "))
                r = int(input("Input r: "))
                num = C(n, r)
                if num == 0:
                    print("The input numbers are wrong.")
                else:
                    print(f"C({n}, {r}) = {num}")
            except:
                print("Please input the number.")
        else:
            print("Please input the command.")

if __name__ == '__main__':
    main()