from continuous_calculus import *
from time import time_ns

class pid:
    def __init__(self, K_p: float, K_i: float, K_d: float) -> None:
        self.__K_p = K_p
        self.__K_i = K_i
        self.__K_d = K_d

        self.i = 0
        self.__e = 0
        self.__t_now = 0
        self.__e_previous = 0
        self.__t_previous = 0

    def __t(self):
        return time_ns() / 1000000

    def __de(self):
        return self.e - self.__e_previous

    def __dt(self):
        return self.__t() - self.__t_previous

    def process(self, y, r) -> float:
        self.e = r - y
        self.__t_now = self.__t()
        self.p = self.__K_p * self.e

        self.i = f_int(self.e, self.__dt(), self.i)
        self.i *= self.__K_i

        self.d = f_deriv(self.__de(), self.__dt())
        if self.d == None:
            self.d = 0
        self.d *= self.__K_d

        u = self.p + self.i + self.d
        self.__e_previous = self.e
        self.__t_previous = self.__t()
        return u