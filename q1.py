def count_pairs(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] == 10:
                count = count+1
    return count

numbers = [2,7,4,1,3,6]
print("No. of pairs : ",count_pairs(numbers))
