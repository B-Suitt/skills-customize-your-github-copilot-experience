def linear_search(arr, target):
    """Return the index of target in arr, or -1 if not found."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr, target):
    """Assume arr is sorted. Return index of target or -1."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(arr):
    """Return a new list with elements of arr sorted (simple bubble sort)."""
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


if __name__ == '__main__':
    # Small manual tests/examples
    data = [3, 1, 4, 1, 5, 9, 2]
    print('linear_search 4 ->', linear_search(data, 4))
    print('linear_search 7 ->', linear_search(data, 7))

    sorted_data = bubble_sort(data)
    print('bubble_sort ->', sorted_data)
    print('equals sorted() ->', sorted_data == sorted(data))

    # binary_search requires sorted input
    print('binary_search 5 ->', binary_search(sorted_data, 5))
    print('binary_search 7 ->', binary_search(sorted_data, 7))
