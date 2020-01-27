while True:
    try:
        Var1=float(input("frist integer\n"))
    except:
        Var1=0
    try:
        Var2=float(input("second integer\n"))
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
    Opsq="square"
    Opsq1="s"
    OpE="exponent"
    OpE1="e"
    Var3=input("what operation would you like? Trying has programmed add(+), subtract(-), multiply(*), divide(/), square(s), and exponent(e)\n")
    if OpA==Var3 or OpA1==Var3:
        print(Var1 + Var2)
    elif OpS==Var3 or OpS1==Var3:
        print(Var1 - Var2)
    elif OpM==Var3 or OpM1==Var3:
        print(Var1 * Var2)
    elif OpD==Var3 or OpD1==Var3:
        print(Var1 / Var2)
    elif Opsq==Var3 or Opsq1==Var3:
        print(Var1 ** Var1)
    elif OpE==Var3 or OpE1==Var3:
        print(Var1 ** Var2)
    else:
        print("Invalid Operation")
