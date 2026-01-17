import subprocess as sp

fan_configuration = "pull"
cpu_loads = [100]
duration_per_load = 80

for load in cpu_loads:
    # record temp before stress test
    temp = int(sp.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True, text=True).stdout.strip()) / 1000
    print(temp)

    # turns on stress test and waits
    stress_process = sp.Popen(["stress-ng", "-q", "--cpu", "4", "--cpu-load", str(load), "--timeout", str(duration_per_load)])
    stress_process.wait()

    # record temp again after stress test
    temp = int(sp.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True, text=True).stdout.strip()) / 1000
    print(temp)