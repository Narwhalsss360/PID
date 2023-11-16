from continuous_calculus import *
from time import time_ns

class pid:
    def __init__(self, K_p: float, K_i: float, K_d: float) -> None:
        self.__K_p = K_p
        self.__K_i = K_i
        self.__K_d = K_d

        self.__i_sum = 0

        self.__e_previous = 0
        self.__t_previous = 0

    def __t(self):
        return time_ns() / 1000000

    def __de(self, e):
        return e - self.__e_previous

    def __dt(self):
        return self.__t() - self.__t_previous

    def process(self, y, r) -> float:
        e = r - y
        u = (self.__K_p * e) + (self.__K_i * f_int(e, self.__dt(), self.__i_sum)) + (self.__K_d * f_deriv(self.__de(), self.__dt()))
        self.__e_previous = e
        self.__t_previous = self.__t()
        return u