#!/usr/bin/env python3
# https://www.pragmaticlinux.com/2020/06/check-the-raspberry-pi-cpu-temperature/

import os


def main():
    """
    Program to demonstrate how to obtain the
    current value of the CPU temperature.
    """
    print(f"Current CPU temperature is "
          f"{get_cpu_temp():.2f} degrees Celsius.\n")


def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature.
    :returns: Current value of the CPU temperature
        if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    """
    The first line in this file holds the CPU temperature
    as an integer times 1000.
    Read the first line and remove the newline character
    at the end of the string.
    """
    if os.path.isfile("/sys/class/thermal/thermal_zone0/temp"):
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            line = f.readline().strip()
        if line.isdigit():
            result = float(line) / 1000
    return result


if __name__ == "__main__":
    main()
