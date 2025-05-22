operador=input("Digite a operação (+, -, *, /): ")
num1=float(input("Digite o valor: "))
num2=float(input("Digite o valor: "))

if operador == "+":
    resultado = (num1+num2)
    print(f"O resultado da adição é {resultado}")
elif operador == "-":
    resultado = (num1-num2)
    print(f"O resultado da subtração é {resultado}")
elif operador == "*":
    resultado = (num1*num2)
    print(f"O resultado da multiplicação foi {resultado}")
elif operador == "/":
    resultado = (num1/num2)
    print(f"O resultado da divisão é {resultado}")
else:
    print("código inválido")


