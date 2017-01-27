#!/usr/bin/env python

from subprocess import Popen
from itertools import islice
import random

threads = 20

randoms = [random.randrange(1, 10) for i in range(0, 200)]

commands = ["sleep %d && print %d" % (j, i) for i, j in enumerate(randoms)]

processes = (Popen(cmd, shell=True) for cmd in commands)

running_processes = list(islice(processes, threads))

while running_processes:
    for i, process in enumerate(running_processes):
        if process.poll() is not None:
            running_processes[i] = next(processes, None)
            if running_processes[i] is None:
                del running_processes[i]
                break



