# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert (len(self.__stack))
        return self.__stack.pop()

    def Max(self):
        assert (len(self.__stack))
        return self.__stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    aux_stack = []
    maxi = -1
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()
        # print("aux_stack", aux_stack)

        if query[0] == "push":
            maxi = max(maxi, int(query[1]))
            # print('maxi:', maxi)
            aux_stack.append((int(query[1]), maxi))
            # print("aux", aux_stack)
            stack.Push((int(query[1]), maxi))

            # if len(aux_stack) == 0:
            #     aux_stack.append((int(query[1]), int(query[1])))
            #     maxi = max(int(query[1]), maxi)
            # else:
            #     if aux_stack[-1] <= int(query[1]):
            #         aux_stack.append(int(query[1]))
            #     elif aux_stack[-1] > int(query[1]):
            #         temp = aux_stack.pop()
            #         aux_stack.append(int(query[1]))
            #         aux_stack.append(temp)
            #     aux_stack.sort()

        elif query[0] == "pop":
            stack.Pop()
            aux_stack.pop()
            # if check == aux_stack[-1]:
            #     aux_stack.pop()
            # aux_stack.sort()
        elif query[0] == "max":
            t, m = stack.Max()
            print(m)
            # temp, maximum = aux_stack[-1]
            # print(maximum)
        else:
            assert 0
