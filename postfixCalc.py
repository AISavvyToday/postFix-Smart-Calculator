from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    for token in infixexpr:
        if token.isdigit() or token.isalpha():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                try:
                    postfixList.append(opStack.pop())
                except:
                    pass
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList

def postfixEval(postfixExpr):
    operandStack = Stack()

    for token in postfixExpr:
        if token.isdigit():
            operandStack.push(int(token))
        elif token.isalpha():
            operandStack.push(token)
        elif token in '/*-+':
            try:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token,operand1,operand2)
                operandStack.push(result)
            except:
                pass
    return int(operandStack.pop())


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

variables_dict = {}
while True:
    inp = input().split()

    nums = []
    for i in inp:
        if '(' in i:
            nums.append(i[0])
            nums.append(i[1])
        elif ')' in i:
            nums.append(i[0])
            nums.append(i[1])
        else:
            nums.append(i)
    if len(nums) == 0:
        continue
    elif len(nums) == 1:
        if nums[0].startswith('-') or nums[0].startswith('+'):
            print(int(nums[0]))
        elif nums[0].endswith('-') or nums[0].endswith('+'):
            print('Invalid expression')


        else:
            if not nums[0].isdigit():
                if '/' in nums[0]:
                    if nums[0] != '/help' and nums[0] != '/exit':
                        print('Unknown command')
                    elif nums[0] == '/help':
                        print('Program for adding/subtracting')
                    elif nums[0] == '/exit':
                        print('Bye!')
                        break

                else:
                    if nums[0].isalpha():
                        if nums[0] in variables_dict:
                            print(variables_dict[nums[0]])
                        else:
                            print('Unknown variable')

                    else:
                        if '=' in nums[0]:
                            variables_dict[nums[0][0]] = nums[0][2]
                        else:
                            print('Invalid identifier')
            else:
                print(int(nums[0]))
    else:
        if nums.count('=') > 1:
            print('Invalid assignment')

        else:
            if nums[0][-1] == '=' or nums[1] == '=' or nums[1][0] == '=':
                new_nums = []
                for num in nums:
                    if '=' in num:
                        num = num.strip('=')
                    new_nums.append(num)
                new_nums = list(filter(None, new_nums))
                if not new_nums[0].isalpha():
                    print('Invalid identifier')
                elif not new_nums[1].isalpha() and not new_nums[1].isdigit():
                    print('Invalid assignment')
                elif new_nums[1].isalpha():
                    if new_nums[1] in variables_dict:
                        variables_dict[new_nums[0]] = variables_dict[new_nums[1]]
                    else:
                        print('Invalid identifier')
                else:
                    variables_dict[new_nums[0]] = new_nums[1]

            else:
                if '(' in nums and ')' not in nums:
                    print('Invalid expression')
                elif ')' in nums and '(' not in nums:
                    print('Invalid expression')
                else:
                    for num in nums:
                        if '*' in num or '/' in num:
                            if len(num) > 1:
                                print('Invalid expression')
                    new_nums = []
                    for num in nums:
                        if num.isalpha():
                            if num in variables_dict:
                                new_num = variables_dict[num]
                                new_nums.append(new_num)
                            else:
                                print('Invalid identifier')
                        else:
                            new_nums.append(num)
                    print(postfixEval(infixToPostfix(new_nums)))
