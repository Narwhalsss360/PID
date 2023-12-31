def f_deriv(dy: float, dx: float) -> float:
    if dx == 0:
        return None
    return dy / dx

def f_int(y:float, dx: float, int_prev: float = 0) -> float:
    int_prev = int_prev + (y * dx)
    return int_prev