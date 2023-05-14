# FCC Course: Scientific Computing with Python
# Project: Arithmetic Formatter
# Author: Wojciech Woźniak
# Date: 10.05.2023


# Defining arithmetic_arranger as function taking two arguments:
# problems - array of strings representing arithmetic problems
# *solve - optional boolean argument for printing solutions
def arithmetic_arranger(problems, solve=False):

    # Check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize empty lists for each line of the problem
    top_nums = []
    bottom_nums = []
    lines = []
    results = []

    # Iterate through each problem in the list of problems
    for problem in problems:
        # Split the problem into its components
        components = problem.split()

        # Check if the problem contains a valid operator (+ or -)
        if components[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if the operands are digits and not greater than 4 digits
        if not (components[0].isdigit() and components[2].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(components[0]) > 4 or len(components[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine the length of the longest operand
        max_length = max(len(components[0]), len(components[2]))

        # Create the top line of the problem
        top_num = components[0].rjust(max_length + 2)
        top_nums.append(top_num)

        # Create the bottom line of the problem
        bottom_num = components[1] + components[2].rjust(max_length + 1)
        bottom_nums.append(bottom_num)

        # Create the line separating the operands and the result
        line = "-" * (max_length + 2)
        lines.append(line)

        # Calculate the result
        result = str(eval(problem))
        results.append(result.rjust(max_length + 2))

    # If solve is True, add the results to the arranged problems
    if solve:
        arranged_problems = "    ".join(top_nums) + "\n" + "    ".join(
            bottom_nums) + "\n" + "    ".join(lines) + "\n" + "    ".join(results)
    else:
        arranged_problems = "    ".join(
            top_nums) + "\n" + "    ".join(bottom_nums) + "\n" + "    ".join(lines)

    return arranged_problems
