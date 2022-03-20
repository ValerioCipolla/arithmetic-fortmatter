def arithmetic_arranger(problems, answer=False):
    # error handling 
    if len(problems) > 5: return "Error: Too many problems."
    for problem in problems:
        if "/" in problem or "*" in problem: return "Error: Operator must be '+' or '-'."
        operand_one = problem.split()[0]
        operand_two = problem.split()[2]
        if len(operand_one) > 4 or len(operand_two) > 4: 
            return "Error: Numbers cannot be more than four digits."
        try:
            int(operand_one)
            int(operand_two)
        except:
            return "Error: Numbers must only contain digits."

    # figure out max length of operand in each problem
    max_length_list = list()
    for problem in problems:
        length_list = []
        operands = problem.split()
        for operand in operands:
            length_list.append(len(operand))
        max_length_list.append(max(length_list))
    
    #build top row
    top_row = "  "
    for problem in problems: 
        operand_one = problem.split()[0]
        operand_two = problem.split()[2]
        operand_one_length = len(problem.split()[0])
        operand_two_length = len(problem.split()[2])
        len_difference = operand_one_length - operand_two_length
        while len_difference < 0:
            top_row = top_row + " "
            len_difference = len_difference + 1
        top_row = top_row + operand_one + "      "
    top_row = top_row.rstrip() + "\n"

    #build bottom row
    bottom_row = ""
    for problem in problems:
        operand_one = problem.split()[0]
        operator = problem.split()[1]
        operand_two = problem.split()[2]
        operand_one_length = len(problem.split()[0])
        operand_two_length = len(problem.split()[2])
        bottom_row = bottom_row + operator
        len_difference = operand_two_length - operand_one_length
        while len_difference < 0:
            bottom_row = bottom_row + " "
            len_difference = len_difference + 1
        bottom_row = bottom_row + " " + operand_two + "    "
    bottom_row = bottom_row.rstrip() + "\n"
    
    #buil dashes
    dashes = ""
    for length in max_length_list:
        while length + 2 > 0:
            dashes = dashes + "-"
            length = length - 1
        dashes = dashes + "    "
    all = top_row + bottom_row + dashes.rstrip()
    print(all)
    return all