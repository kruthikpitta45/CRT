def Linear_Time(arr):
    for i in arr:
        print(i)

print(Linear_Time([10, 20, 30, 40, 50]))  # O(n)


def Quadratic_Time(arr):
    for i in arr:
        for j in arr:
            print(i)

print(Quadratic_Time([10, 20, 30, 40, 50]))  # O(n^2)


def linearithmic_time(arr):
    return sorted(arr)

print(linearithmic_time([10, 20, 30, 10, 50, 20]))  # O(n log n)


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

n = int(input())
print(fibo(n))  # O(2^n)