import subprocess as sp

fan_configuration = "pull"
cpu_loads = [0, 25, 50, 75, 100]
duration_per_load = 60

with open(f"{fan_configuration}.csv", "w") as f:
    f.write("load,tempC\n")

    for load in cpu_loads:

        # record temp before stress test
        temp = int(sp.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True, text=True).stdout.strip()) / 1000
        f.write(f"{load},{temp:.1f}\n")

        # turns on stress test and waits
        stress_process = sp.Popen(["stress-ng", "--cpu", "4", "--cpu-load", str(load), "--timeout", str(duration_per_load)])
        stress_process.wait()

        # record temp again after stress test
        temp = int(sp.run(["cat", "/sys/class/thermal/thermal_zone0/temp"], capture_output=True, text=True).stdout.strip()) / 1000
        f.write(f"{load},{temp:.1f}\n")