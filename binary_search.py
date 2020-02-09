# test
def binary_search(arr, target):
    left, right = 0, len(arr) -1
    while left < right -1:
        mid = (left + right)/2
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid
        else:
            return mid
    if arr[left] == target:
        return left
    return right

if __name__ == '__main__':
    arr = [1, 3, 4,5, 23, 412, 451,512, 5121,12312 ,12232312]
    tar_index = binary_search(arr, 512)
    print(tar_index)
    print(arr[tar_index])
