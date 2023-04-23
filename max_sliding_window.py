# python3

from collections import deque


def max_sliding_window_naive(nums, k):
    d = deque()
    n = len(nums)
    result = []
    for i in range(k):
        while d and nums[i] >= nums[d[-1]]:
            d.pop()
        d.append(i)

    for i in range(k, n):
        result.append(nums[d[0]])
        while d and d[0] <= i - k:
            d.popleft()
        while d and nums[i] >= nums[d[-1]]:
            d.pop()
        d.append(i)
    result.append(nums[d[0]])
    return result


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

