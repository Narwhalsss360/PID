from log_dict import *
from pid import *
from continuous_calculus import *

def f(x):
    return x ** 2

#region Logger Test
xy_samples = [(x / 10, f(x / 10)) for x in range(0, 51, 1)]
xy_data = { 'x': [x for x, y in xy_samples], 'y': [y for x, y in xy_samples]}
#endregion

#region Continuous Calculus Test
xy_deriv = []
for i, (x, y) in enumerate(xy_samples):
    if i == 0:
        xy_deriv.append((x, 0))
        continue
    x_prev, y_prev = xy_samples[i - 1]
    xy_deriv.append((x, f_deriv(y - y_prev, x - x_prev)))

xy_data['f\'(x)'] = [ df for x, df in xy_deriv]

xy_int = []
int_sum = 0
for i, (x, y) in enumerate(xy_samples):
    if i != 0:
        x_prev, y_prev = xy_samples[i - 1]
        int_sum = f_int(y, x - x_prev, int_sum)
    xy_int.append((x, int_sum))
    
xy_data['integral(f(x)dx)'] = [ int for x, int in xy_int]
#endregion

with open('xy_test_data.csv', 'w') as file:
    log_dict_csv(file, xy_data)

controller = pid(1, 1, 1)