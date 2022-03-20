def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5: return "Error: Too many problems."
    for problem in problems:
        if "/" in problem or "*" in problem: return "Error: Operator must be '+' or '-'."
    return answer