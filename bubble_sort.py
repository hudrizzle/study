"""
bubble sort

Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

"""
# swap the adjacent elements to the right.

def bubble_sort(arr):
    if len(arr) <= 1:
        return arr

    # compar i with i +1, swap if i+1 < i
    for j in range(len(arr) -1):
        end_index = len(arr) -1 -j
        for i in range(end_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


if __name__ == "__main__":
    arr = [12,123,12 ,12,312,31,231,23,12,31,23,12, 12,31,231]
    arr = []
    print bubble_sort(arr)
