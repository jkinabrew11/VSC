def binary_search(arr, target_val):
    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target_val:
            return mid

        elif arr[mid] < target_val:
            left = mid + 1
        
        else:
            right = mid - 1

    return -1