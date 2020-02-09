# given a number,

# two operations: + 1 and *2
# show all the numbers of the shortest path to the nubmer
"""
if num is odd, -1
if num is even, /2

if num is 0, end



"""
def shortest_path(num):
    if num < 0:
        return "error input"

    path = []
    while num > 0:
        path.append(num)
        if num%2 ==0:
            num = num // 2
        else:
            num -= 1
    # path = path.reverse()
    return path[::-1]

if __name__ == "__main__":
    num = 1231231
    spath = shortest_path(num)
    print(spath)
