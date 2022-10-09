def factorial(number):
    if (number == 0):
        return 1
    elif number < 0:
        return 0

    sum = 1
    for i in range(1, number + 1, 1):
        sum *= i
    return sum

def main():
    while(True):
        user_input = input("Input '/stop' or number: ")
        if (user_input == "/stop"):
            exit()
        else:
            try:
                ans = factorial(int(user_input))
                if (ans):
                    print(f"{user_input}! = {ans}")
                else:
                    print("The number is wrong.")
            except ValueError:
                print("Please input the command or number.")

if __name__ == '__main__':
    main()