from continuous_calculus import *
from time import time_ns

class pid:
    def __init__(self, K_p: float, K_i: float, K_d: float) -> None:
        self.__K_p = K_p
        self.__K_i = K_i
        self.__K_d = K_d

        self.p = 0
        self.i = 0
        self.d = 0
        self.__e = 0

        self.y = None
        self.r = None

        self.__t_now = 0

        self.__T_START = None
        self.__e_previous = 0
        self.__t_previous = 0

    def __t(self) -> float:
        if self.__T_START is None:
            self.__T_START = time_ns()
        return (time_ns() - self.__T_START) / 1e9

    def __de(self) -> float:
        return self.e - self.__e_previous

    def __dt(self) -> float:
        return self.__t() - self.__t_previous

    def process(self, y, r) -> float:
        self.r = r
        self.y = y
        self.e = y - r
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