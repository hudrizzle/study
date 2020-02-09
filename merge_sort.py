"""
merge sort two lists
"""
# arr1 = [1, 3, 4, 5, 6]
# arr2 = [2, 4, 5, 6, 7]

def merge_sorted_list(arr1, arr2):
    i, j = 0, 0
    merged_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_list.append(arr1[i])
            # print arr1[i]
            i += 1
        else:
            merged_list.append(arr2[j])
            # print arr2[j]
            j += 1
    # one of the array reach its end
    if i< len(arr1):
        merged_list.extend(arr1[i:])
    else:
        merged_list.extend(arr2[j:])

    return merged_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)/2
    left_arr, right_arr = arr[:mid], arr[mid:]
    sort_left, sort_right = merge_sort(left_arr), merge_sort(right_arr)
    # print merge_sorted_list(sort_left, sort_right)
    return merge_sorted_list(sort_left, sort_right)

if __name__ == "__main__":
    arr = [12,123,12 ,12,312,31,231,23,12,31,23,12, 12,31,231]
    # arr = []
    arr1 = [1, 3, 4, 5, 6, 10]
    arr2 = [2, 1231]
    # print merge_sorted_list(arr1, arr2)
    print merge_sort(arr)
