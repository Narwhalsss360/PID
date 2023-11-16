from log_dict import *
from pid import *
from continuous_calculus import *
from sample import *

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

with open('xy_test_data.csv', 'w') as file:
    log_dict_csv(file, xy_data)
#endregion

#region Samples Test
sample_log = {}
for x_scaled in range(0, 100):
    x = x_scaled / 10
    coordinate = sample(x, f(x))
    vars_log(coordinate, sample_log, ('t', time_ns()))

with open('samples.csv', 'w') as samples_file:
    log_dict_csv(samples_file, sample_log)
#endregion

controller = pid(1, 1, 1)
controller_log = {}
#region Controller Log Test
for x_scaled in range(0, 100):
    x = x_scaled / 10
    out = controller.process(x, 0)
    vars_log(controller, controller_log, ('out', out))

with open('controller_test.csv', 'w') as controller_log_file:
    log_dict_csv(controller_log_file, controller_log)
#endregion

exit()