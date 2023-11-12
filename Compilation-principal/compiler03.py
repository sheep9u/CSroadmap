# 算符优先关系表
precedence = {
    '+': {'+': '>', '*': '<', '(': '<', ')': '>', '$': '>'},
    '*': {'+': '>', '*': '>', '(': '<', ')': '>', '$': '>'},
    '(': {'+': '<', '*': '<', '(': '<', ')': '=', '$': ''},
    ')': {'+': '>', '*': '>', '(': '',  ')': '>', '$': '>'},
    '$': {'+': '<', '*': '<', '(': '<', ')': '',  '$': ''}
}

def is_operand(c):
    return c.isalpha() or c.isdigit()  # 检查是否是操作数（字母或数字）

def parse_expression(input_tokens):
    stack = ['$']
    input_tokens.append('$')

    while stack and input_tokens:
        top = stack[-1]
        current = input_tokens[0] if input_tokens else '$'
        print("Stack:", stack, "Input:", input_tokens)  # 打印当前栈和输入状态

        if top == '$' and current == '$':
            print("Accept")
            break
        elif is_operand(top) or is_operand(current):  # 如果栈顶或当前元素是操作数
            stack.append(input_tokens.pop(0))  # 直接移进
        elif precedence[top][current] == '<' or precedence[top][current] == '=':
            stack.append(input_tokens.pop(0))
        elif precedence[top][current] == '>':
            stack.pop()  # 执行规约操作
        else:
            print("Error")
            break

# 测试
input_tokens = list("(a+b)*c")
parse_expression(input_tokens)
