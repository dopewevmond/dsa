def check_validity(bracket):
    my_stack = []

    for char in bracket:
        if char in ['(', '[']:
            my_stack.append(char)
        else:
            if len(my_stack) == 0:
                return False
            top = my_stack.pop()
            if (top == '[' and char != ']') or (top == '(' and char != ')'):
                return False
    return len(my_stack) == 0


print(check_validity('(())(()()()')) # should return False
print(check_validity('(())(()()()(()))')) # should return True