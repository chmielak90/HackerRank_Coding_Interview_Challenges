def is_matched(expression):
    stack = []
    dicty = {'(': ')', '[': ']', '{': '}'}
    for x in expression:
        # print(stack)
        if dicty.get(x):
            stack.append(dicty[x])
        else:
            if len(stack) == 0 or x != stack[len(stack)-1]:
                return False
            stack.pop()
    return len(stack) == 0


print(is_matched('({[()]})'))
print(is_matched('({[}])'))