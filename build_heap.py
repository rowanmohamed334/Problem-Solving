# python3
def parent(i):
    return (i-1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


counter = 0
output = []


def shift_down(i, data):
    global counter
    global output
    size = len(data)
    min_index = i
    # print("i: ", i, data[i])
    left = left_child(i)
    # print('left:', left)
    if left < size and data[left] < data[min_index]:
        min_index = left
        # print('left in:', left, data[left])
    right = right_child(i)
    # print('right:', right)
    if right < size and data[right] < data[min_index]:
        min_index = right
        # print('right in:', right, data[right])
    # print("before swap ", )
    if i != min_index:
        counter += 1
        output.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        shift_down(min_index, data)


def build_heap(data):

    n = len(data)
    for i in range(n // 2, -1, -1):
        # print("the out loop", i)
        # print(left_child(i))
        # print(right_child(i))
        shift_down(i, data)
    # print('counter test:', counter)
    if counter:
        print(counter)
    else:
        print(0)
    if len(output):
        for i, j in output:
            print(i, j)
    # print('output test: ', output)
    # print("result: ", data)
    #
    return 0


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    # print(len(swaps))
    # for i, j in swaps:
    #     print(i, j)


if __name__ == "__main__":
    main()
