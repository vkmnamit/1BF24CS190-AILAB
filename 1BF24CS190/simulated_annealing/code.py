import random
import math

def f(x):
    return x * x

def main():
    x = float(input("Enter initial x: "))
    T = float(input("Enter initial temperature: "))
    alpha = float(input("Enter cooling rate (0 to 1): "))

    if T <= 0 or not 0 < alpha < 1:
        print("Invalid input")
        return

    best = x

    while T > 0.1:
        new_x = x + random.uniform(-1, 1)
        delta = f(new_x) - f(x)

        if delta < 0 or random.random() < math.exp(-delta / T):
            x = new_x

        if f(x) < f(best):
            best = x

        T = T * alpha

    print("Best solution:", best)
    print("Minimum value:", f(best))

if __name__ == "__main__":
    main()