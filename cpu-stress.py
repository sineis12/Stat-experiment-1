import subprocess as sp
import time

timer_minutes = 10
cpu_loads = [100]
duration_per_load = 120

#functions
def uptime_minutes():
    with open("/proc/uptime") as f:
        return float(f.read().split()[0]) / 60
    
def read_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return int(f.read()) / 1000

#timer

while uptime_minutes() < timer_minutes:
    time.sleep(5)

#actual experiment
for load in cpu_loads:
    # record temp before stress test
    print(read_cpu_temp())

    # turns on stress test and waits
    stress_process = sp.Popen(["stress-ng", "-q", "--cpu", "4", "--cpu-load", str(load), "--timeout", str(duration_per_load)])
    stress_process.wait()

    # record temp again after stress test
    print(read_cpu_temp())
