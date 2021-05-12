import serial.tools.list_ports
import time
t0 = time.time()
print(list(serial.tools.list_ports.comports(include_links=False)))
te = time.time()
print("time taken:", round(te-t0,2))