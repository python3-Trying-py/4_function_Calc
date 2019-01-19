while True:
    try:
        Var1=int(input("frist integer\n"))
    except:
        Var1=0
    try:
        Var2=int(input("second integer\n"))
    except:
        Var2=0
    OpA="add"
    OpA1="+"
    OpS="subtract"
    OpS1="-"
    OpM="multiply"
    OpM1="*"
    OpD="divide"
    OpD1="/"
    Var3=input("what operation would you like?\n")
    if OpA==Var3 or OpA1==Var3:
        print(Var1 + Var2)
    elif OpS==Var3 or OpS1==Var3:
        print(Var1 - Var2)
    elif OpM==Var3 or OpM1==Var3:
        print(Var1 * Var2)
    elif OpD==Var3 or OpD1==Var3:
        print(Var1 // Var2)
    else:
        print("Invalid Operation")
