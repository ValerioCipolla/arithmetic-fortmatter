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
    no_answer_solution = top_row + bottom_row + dashes.rstrip()

    # if answer is needed buil answer row
    with_answer_solution = no_answer_solution + "\n"
    index = 0
    for problem in problems:
        operand_one = int(problem.split()[0])
        operator = problem.split()[1]
        operand_two = int(problem.split()[2])
        if operator == "+":
            solution = operand_one + operand_two
        elif operator == "-":
            solution = operand_one - operand_two
        solution_length = len(str(solution))
        number_of_dashes = max_length_list[index] + 2
        index = index + 1
        while number_of_dashes > solution_length:
            with_answer_solution = with_answer_solution + " "
            number_of_dashes = number_of_dashes - 1
        with_answer_solution = with_answer_solution + str(solution) + "    "
    with_answer_solution = with_answer_solution.rstrip()

    if answer is False:
        return no_answer_solution
    else:
        return with_answer_solution