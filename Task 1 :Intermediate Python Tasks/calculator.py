#Custom Exception
class FormulaError(Exception):
    pass


#Calculation Function
def calculate_formula(formula):
    parts = formula.split()

    if len(parts) != 3:
        raise FormulaError("Input must consist of exactly 3 elements")
    

    try:
        num1 = float(parts[0])
        num2 = float(parts[2])
    except ValueError:
        raise FormulaError("The 1st and 3rd elements must be valid numbers.")
    

    operator = parts[1]
    if operator not in ['+', '-','*','/']:
        raise FormulaError("The operator must be either '+' or '-' or '*' or '/'")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result= num1/num2
    return result


#Main Function
def interactive_calculator():

    while True:

        form = input("Enter a formula (e.g., '1 + 1') or type quit: ").strip()

        if form.lower() == 'quit':
            print("Exiting the calculator. Goodbye..!")
            break

        try:
            result = calculate_formula(form)
            print(f"Result: {result}")
        except FormulaError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

interactive_calculator()