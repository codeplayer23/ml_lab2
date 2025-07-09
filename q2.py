def rangedef():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    max_val = max(numbers)
    min_val = min(numbers)
    a = [max_val,min_val]
    return a

print(rangedef())