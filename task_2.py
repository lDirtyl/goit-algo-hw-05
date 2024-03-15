def binary_search_with_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None
    
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            upper_bound = arr[mid]
            break

    # знаходимо верхню межу
    if upper_bound is None:
        if low < len(arr):
            upper_bound = arr[low]
        else:
            upper_bound = None
    
    return (iterations, upper_bound)

# Тестування функції
arr = [1.5, 3.2, 4.7, 5.6, 7.0, 8.8, 9.9]
x = 5.6
result = binary_search_with_upper_bound(arr, x)
print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")