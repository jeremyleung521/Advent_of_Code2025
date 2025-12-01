# perf.py
#
# Calculates performance...

import time

def calc_perf(function):
    startTime = time.time()
    startTimeCPU = time.process_time()
    function
    print(f'Wall Clock: {(time.time() - startTime)} sec')
    print(f'CPU Time: {(time.process_time() - startTimeCPU)} sec')