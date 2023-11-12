def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
    stack = []
    postfix = []
    number_buffer = []

    def flush_number_buffer():
        if number_buffer:
            postfix.append(''.join(number_buffer))
            number_buffer.clear()

    for char in expression:
        if char.isnumeric():
            number_buffer.append(char)
        else:
            flush_number_buffer()
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack:
                    stack.pop()  # Pop '(' from stack
            else:  # Operator
                while stack and precedence[stack[-1]] >= precedence[char]:
                    postfix.append(stack.pop())
                stack.append(char)

    flush_number_buffer()
    while stack:
        postfix.append(stack.pop())

    return postfix

def calculate_postfix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)

    return stack.pop()

# Main program
expression = "21+((42-2)*15+6))-18#".replace("#", "").replace("&", "")
postfix = infix_to_postfix(expression)
postfix_str = ' '.join(postfix)  # Changed for better readability
result = calculate_postfix(postfix)

print("原来表达式：", expression)
print("后缀表达式：", postfix_str)
print("计算结果：", result)
