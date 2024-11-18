operator = None
operand1 = None
operand2 = None
result = None

def main():
    ask_user_input()
    calcul()
    resultat()


def ask_user_input():
    # Get first operand from the user
    global operand1, operator, operand2
    operand1 = float(input("Enter the first operand: "))
    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")
    # Get second operand from the user
    operand2 = float(input("Enter the second operand: "))


def calcul():
    global result
    match operator:
        case '+':
            result = operand1 + operand2
        case '-':
            result = operand1 - operand2
        case '*':
            result = operand1 * operand2

        case '/':
            if operand2 != 0:
                result = operand1 / operand2
            else:
                result = None
        case _:
            print("Ce n'est pas un +,-,/,*")
            result = None

def resultat():
    if result is not None and operator != '/':
        print(f"Le résultat de {int(operand1)} {operator} {int(operand2)} est {int(result)}")
    if result is not None and operator == '/':
        print(f"Le résultat de {int(operand1)} {operator} {int(operand2)} est {result}")
    else:
        if operator == '/' and operand2 == 0:
            print("Division par zéro impossible")
        else:
            print("Opérateur invalide")
# Call the main function to run the program
main()