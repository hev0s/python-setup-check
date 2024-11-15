def math():
    from src.Opérations.add import addition
    from src.Opérations.sous import soustraction
    from src.Opérations.divi import division
    from src.Opérations.mult import multiplication
    from src.Opérations.puiss import puissance
    from src.Opérations.racine import racine
    from src.Opérations.pourc import pourcentage
    op = 0
    a = 0
    b = 0
    if op == "+":
        print(addition(a, b))
    if op == "-":
        print(soustraction(a, b))
    if op == "*":
        print(multiplication(a, b))
    if op == "/":
        print(division(a, b))
    if op == "^":
        print(puissance(a, b))
    if op == "v":
        print(racine(a, b))
    if op == "%":
        print(pourcentage(a, b), "%")
    return math()
