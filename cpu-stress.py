import subprocess as sp

fan_configuration = "pull"
cpu_loads = [0, 25, 50, 75, 100]
duration_per_load = 60

for load in cpu_loads:
    stressProcess = sp.Popen(["stress-ng", "--cpu", "4", "--cpu-load", str(load), "--timeout", str(duration_per_load)])
    