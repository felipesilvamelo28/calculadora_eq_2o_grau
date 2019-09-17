class Function:
    __a: int
    __b: int
    __c: int

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    @a.setter
    def a(self, value):
        try:
            self.__a = int(value)
        except Exception:
            print("Valor de A é inválido")
            exit()

    @b.setter
    def b(self, value):
        try:
            self.__b = int(value)
        except Exception:
            print("Valor de B é inválido")
            exit()

    @c.setter
    def c(self, value):
        try:
            self.__c = int(value)
        except Exception:
            print("Valor de C é inválido")
            exit()

    def soma(self):
        sum = self.__a + self.__b + self.__c
        return sum