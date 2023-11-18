"""Serial Controller"""
import atexit
import serial
from pid import pid
from log_dict import vars_log, log_dict_csv

LOG_FILE_NAME = "serial_controller.log"

BAUD = 115200
PORT_NAME = "COM4"

serial_controller_vars = {}
serial_controller = pid(1, 1, 1)
port = serial.Serial(PORT_NAME, BAUD)
port.open()

def exitting() -> None:
    """Cleans up program before exitting"""
    port.close()
    with open(LOG_FILE_NAME, 'w', encoding='utf-8') as log_file:
        log_dict_csv(log_file, serial_controller_vars)

atexit.register(exitting)

SET_POINT = 0

while True:
    process_variable = float(str(port.readline()))
    out = serial_controller.process(process_variable, SET_POINT)
    vars_log(serial_controller, serial_controller_vars, ('out', out))