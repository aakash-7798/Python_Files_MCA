
# Written by Aakash Nadupalli

# 7. Write a Python program that uses stack to convert a fully parenthesized arithmetic
# expression from infix to postfix.


def precedence(ch):
    if ch == "+" or ch == "-":
        return 0
    elif ch == "*" or ch == "/":
        return 1
    elif ch == "^":
        return 2
    return -1

def convert_infix_to_postfix(exps):
    stck = []
    postfix_expression = " "

    for i in list(exps):
        ch = i

        if ch.isalpha():
            postfix_expression += ch

        elif ch == '(':
            stck.append(ch)

        elif ch == ')':
            while stck != [] and stck[-1] != "(":
                postfix_expression += stck.pop()
            stck.pop()

        else:
            while stck != [] and precedence(ch) <= precedence(stck[-1]):
                postfix_expression += stck.pop()
            stck.append(ch)

    while stck != []:
        if stck[-1] == '(':
            return "Invalid Expression"
        postfix_expression += stck.pop()

    return postfix_expression

print(convert_infix_to_postfix("(a+b)*(c/d)"))
print(convert_infix_to_postfix("a+b*c/d"))