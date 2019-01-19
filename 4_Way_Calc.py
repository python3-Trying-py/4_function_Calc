while True:
    Var1=int(input("frist integer\n"))
    Var2=int(input("Second integer\n"))
    OpA="add"
    OpA1="+"
    OpS="subtract"
    OpS1="-"
    OpM="multiply"
    OpM1="*"
    OpD="divide"
    OpD1="/"
    Var3=input("what operation would you like?\n")
    if OpA==Var3:
        print(Var1 + Var2)
    elif OpA1==Var3:
        print(Var1 + Var2)
    elif OpS==Var3:
        print(Var1 - Var2)
    elif OpS1==Var3:
        print(Var1 - Var2)
    elif OpM==Var3:
        print(Var1 * Var2)
    elif OpM1==Var3:
        print(Var1 * Var2)
    elif OpD==Var3:
        print(Var1 / Var2)
    elif OpD1==Var3:
        print(Var1 / Var2)
    else:
        print("Invalid Operation")
