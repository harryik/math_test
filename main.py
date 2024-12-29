import random

Operators = ["+", "-", "*"]
MinOperand = 3
MaxOperand = 12

def generate_problem():
    left = random.randint(MinOperand, MaxOperand)
    right = random.randint(MinOperand, MaxOperand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " "+ str(right)
    print(expr)
    return  expr

generate_problem()