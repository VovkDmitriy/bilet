def mainFunc():
    print("Enter *n*: ")
    n = int(input())
    i = 1
    print("Result: ", end="")
    while(i <= n):
        print(calculate(i), ", ", end="")
        i = i + 1


def calculate(n):
    an = a1 + d * (n - 1)
    return an



d = 2
a1 = 5
if __name__ == '__main__':
    mainFunc()