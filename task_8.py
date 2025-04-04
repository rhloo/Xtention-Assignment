
def quick_sort(arr):
    if len(arr)<=1:
       return arr

    pivot=arr[len(arr) // 2]
    print(pivot)
    left=[i for i in arr if i<pivot]
    print(left)
    center=[i for i in arr if i==pivot]
    print(center)
    right=[i for i in arr if i>pivot]
    print(right)
    print()
    return quick_sort(left) + center + quick_sort(right)
print(quick_sort([82,6,99,3,9,11]))