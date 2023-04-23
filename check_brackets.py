# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for i, next in enumerate(text):
        # print('enter')
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((next, i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) != 0:
                temp, index = opening_brackets_stack.pop()
                if pairs[temp] != next:
                    return i+1
            else:
                return i+1
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        lats_item, last_index = opening_brackets_stack.pop()
        # print('e:' ,lats_item, last_index)
        return last_index + 1
    # return 'Success' if len(opening_brackets_stack) == 0 else len(text

def main():
    text = input()
    mismatch = find_mismatch(text)

    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
