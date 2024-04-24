#selection sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Sorting the array
sorted_arr = selection_sort(arr)

# Output the sorted array
print(*sorted_arr)


#bubble sort
n = int(input())
l = list(map(int, input().split()))


fixThis = n - 1
while fixThis > 0:
   for index in range(fixThis):
       if l[index] > l[index + 1]:
           l[index], l[index + 1] = l[index + 1], l[index]
   fixThis -= 1
print(*l)

#insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Sorting the array
sorted_arr = insertion_sort(arr)

# Output the sorted array
print(*sorted_arr)


#merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the two sorted arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Sorting the array
sorted_arr = merge_sort(arr)

# Output the sorted array
print(*sorted_arr)

#quick sort 1
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Sorting the array
quick_sort(arr, 0, n - 1)

# Output the sorted array
print(*arr)

