import math


class Calcula:
    __x1: int
    __x2: int
    __delta: float

    def calcula_delta(self, function):
        a = function.a
        b = function.b
        c = function.c
        delta = ((b * b) - (4 * a * c))
        self.__delta = delta

        if self.__delta < 0:
            print("Delta negativo, a função não possui raízes.")
            exit()

    def calcula_raiz_1(self, function):
        a = function.a
        b = function.b
        delta = self.__delta

        try:
            self.__x1 = ((- b) + math.sqrt(delta)) / (2 * a)
        except ZeroDivisionError:
            print("Erro. Não existe divisão por zero.")
            exit()

    def calcula_raiz_2(self, function):
        a = function.a
        b = function.b
        delta = self.__delta
        try:
            self.__x2 = ((- b) - (math.sqrt(delta))) / (2 * a)
        except ZeroDivisionError:
            print("Erro. Não existe divisão por zero.")
            exit()

    def imprime(self):
        return print("Valor de x1= {}; Valor de x2 = {}".format(self.__x1, self.__x2))