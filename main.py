from function import Function
from calc import Calcula

print("################################################")
print("CALCULADORA DAS RAÍZES DE UMA EQUAÇÃO DO 2o GRAU")
print("################################################")

function = Function(input("Digite o valor de A: "), input("Digite o valor de B: "), input("Digite o valor de C: "))
calcula = Calcula()


calcula.calcula_delta(function)
calcula.calcula_raiz_1(function)
calcula.calcula_raiz_2(function)

calcula.imprime()
