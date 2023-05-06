def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", "", ""]

    for problem in problems:
        # Split the problem string into its constituent parts
        operands = problem.split()
        operand1 = operands[0]
        operator = operands[1]
        operand2 = operands[2]

        # Check if the operator is valid
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        # Check if the operands contain only digits and have at most four digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the width of the problem and add it to the arranged problems
        width = max(len(operand1), len(operand2)) + 2
        arranged_problems[0] += operand1.rjust(width) + "    "
        arranged_problems[1] += operator + " " + operand2.rjust(width - 2) + "    "
        arranged_problems[2] += "-" * width + "    "

        # If requested, compute and add the answer to the arranged problems
        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            arranged_problems[3] += answer.rjust(width) + "    "

    # Join the arranged problems into a single string and return it
    arranged_problems = "\n".join(arranged_problems)
    if show_answers:
        arranged_problems += "\n"
    return arranged_problems
