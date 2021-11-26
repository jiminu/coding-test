from itertools import permutations
import re

def solution(expression):
    answer= []
    # operator = list(permutations(['+','-','*']))
    operator = [['*','-','+']]

    for oper in operator :
        exp = expression
        for i in range(len(oper)) :
            if i == 2 :
                calc = f'-?\d+\{oper[i]}-?\d+'
                # calc = '-?\d+\{}-?\d+'.format(oper[i])
            else :
                calc = f'\d+\{oper[i]}-?\d+'
                # calc = '\d+\{}\d+'.format(oper[i])
            p = re.search(calc, exp)
            while p :
                calc_exp = p.group()
                result = eval(calc_exp)
                
                exp = exp.replace(calc_exp, str(result))
                p = re.search(calc, exp)
        answer.append(abs(int(exp)))
            
    return max(answer)

s = "50*6-3*-2"

print(solution(s))
print(eval('-100*-180'))