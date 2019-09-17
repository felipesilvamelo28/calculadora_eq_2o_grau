from function import Function
from calc import Calcula

print("################################################")
print("CALCULADORA DAS RAÍZES DE UMA EQUAÇÃO DO 2o GRAU")
print("################################################")

function = Function()
calcula = Calcula()

function.a = input("Digite o valor de A: ")
function.b = input("Digite o valor de B: ")
function.c = input("Digite o valor de C: ")


calcula.calcula_delta(function)
calcula.calcula_raiz_1(function)
calcula.calcula_raiz_2(function)

calcula.imprime()
