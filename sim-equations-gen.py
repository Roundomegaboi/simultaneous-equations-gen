#python simultaneuous equations generator
from random import randint

def gen_coeffs(low,up):
    return randint(low, up), randint(low, up)

#completely random selection
def add_extra(ans1,ans2):
    decider = randint(1,3)
    if decider == 1:
        return 0, 0, ans1, ans2
    
    elif decider == 2:
        decider = randint(1,2)
        amount = randint(1,20)
        if decider == 1:
            amount = -amount
        return amount, 0, ans1+amount, ans2
    
    elif decider == 3:
        amount1 = randint(1,20)
        amount2 = randint(1,20)
        decider = randint(1,3)
        if decider == 1:
            amount1 = -amount1
            amount2 = -amount2
        elif decider == 2:
            amount1 = -amount1
        
        return amount1, amount2, ans1 + amount1, ans2 + amount2
        
def finish_equation(extra, equation, ans):
    if extra != 0:
        if extra < 0:
            equation += ' - ' + str(-extra)
        else:
            equation += ' + ' + str(extra)
    equation += ' = ' + str(ans)
    return equation

x = randint(0,5)
y = randint(0,5)

coeff_x_1, coeff_x_2 = gen_coeffs(1,15)
coeff_y_1, coeff_y_2 = gen_coeffs(1,15)

ans_q_1 = (coeff_x_1 * x) + (coeff_y_1 * y)
ans_q_2 = (coeff_x_2 * x) + (coeff_y_2 * y)

extra1,extra2, ans_q_1, ans_q_2 = add_extra(ans_q_1, ans_q_2)

equation1 = f'{coeff_x_1}x + {coeff_y_1}y'
equation1 = finish_equation(extra1, equation1, ans_q_1)

equation2 = f'{coeff_x_2}x + {coeff_y_2}y'
equation2 = finish_equation(extra2, equation2, ans_q_2)

print(equation1)
print(equation2)
print('x = ', x)
print('y = ', y)
