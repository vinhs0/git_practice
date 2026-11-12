def printHello():
    print("Yel")

def countToN(n):
    for i in range(n):
        print(i)
    print("Merge Conflict")

def rebaseTest():
    print("Step 2")
    def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            f1=0
            f2=1
            f=0
            for i in range(2,n+1):
                f=f1+f2
                if i%2:
                    f1=f
                else:
                    f2=f
            return f

if __name__ == "__main__":
    countToN(4)