def find_pairs_with_sum(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append(f"{arr[i]},{arr[j]}")
    return "\n".join(pairs)

 
array1 = [1, 2, 3, 4, 5]
sum1 = 5
result1 = find_pairs_with_sum(array1, sum1)
print(result1)

array2 = [1, 2, 3, 4, 5]
sum2 = 4
result2 = find_pairs_with_sum(array2, sum2)
print(result2)
