import random

def mean_median():
    n = 25
    numbers = [random.randint(1,10) for _ in range(n)]
    sum = 0
    for i in range(n):
        sum = sum+numbers[i]
    mean = sum/n

    numbers.sort()
    if n%2==0:
        median = (numbers[n//2] + numbers[(n//2)+1])//2
    else:
        median = (numbers[(n+1)//2])

    a = [mean,median]
    return a

print(mean_median())