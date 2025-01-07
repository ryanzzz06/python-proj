from random import randint

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def math_challenge_factorial():
    n=randint(1,10)
    t=int(input("calculate the factorial of", str(n)))
    if t==factorial(n):
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect! the correct answer is", factorial(n))
        return False

def solve_linear_equation():
    b=randint(1,10)
    a=randint(1,10)
    x=-b/a
    L=[a,b,x]
    return L

def math_challenge_equation():
    sol=solve_linear_equation()
    print ("Math challenge: solve the equation: ", str(sol[0]), "x + ", str(sol[1]), "=0")
    k=float(input("What is the value of x:"))
    if k==sol[2]:
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect! the correct answer is", sol[2])
        return False

def is_prime(n):
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def nearest_prime(n):
    if is_prime(n)==True:
        return n
    else:
        while is_prime(n)==False:
            n=n+1
        return n

def math_challenge_prime():
    n=randint(10,20)
    f=int(input("What is the prime number closest to ", str(n),": "))
    if f==nearest_prime(n):
        print("Correct! You win a key")
        return True
    else:
        print("Incorrect! the correct answer is", nearest_prime(n))
        return False

def math_challenge():
    challenges=[math_challenge_factorial, math_challenge_equation, math_challenge_prime]
    challenge=challenges[randint(0,len(challenges)-1)]
    challenge()
