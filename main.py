import random
import time

Operators = ["+", "-", "*"]
MinOperand = 1
MaxOperand = 10
TotalProblems = 10

def generate_problem():
    left = random.randint(MinOperand, MaxOperand)
    right = random.randint(MinOperand, MaxOperand)
    operator = random.choice(Operators)

    expr = str(left) + " " + operator + " "+ str(right)
    answer = eval(expr)
    return  expr, answer

wrong = 0

start_time = time.time()
input("Press enter to start")

for i in range(TotalProblems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i +1) + ": \n" + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("Your time is",total_time,"seconds")
print("You had",wrong,"wrong answers.")