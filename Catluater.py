first = float(input("Enter first Number => "))
sec = float(input("Enter Second Number => "))
opr = str(input("Enter Operation (+ Plus, - Minus, * Times, / Division) => "))

if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total = str("Please Enter a Valid Operation")

print (total)
input("Press the enter key to exit!")