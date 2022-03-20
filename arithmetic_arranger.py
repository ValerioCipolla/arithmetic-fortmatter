def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5: return "Error: Too many problems."
    for problem in problems:
        if "/" in problem or "*" in problem: return "Error: Operator must be '+' or '-'."
        operand_one = problem.split()[0]
        operand_two = problem.split()[2]
        if len(operand_one) > 4 or len(operand_two) > 4: 
            return "Error: Numbers cannot be more than four digits."
        try:
            int_one = int(operand_one)
            int_two = int(operand_two)
        except:
            return "Error: Numbers must only contain digits."

        
    return answer