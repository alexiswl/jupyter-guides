#!/usr/bin/env python

from subprocess import Popen
from itertools import islice
import random

threads = 5

files = ["output.file%d" % i for i in range(0, threads)]

file_handlers = []
for i, handler in enumerate(file_handlers):
    handler = open('output.%d' % i, 'w')

for handler in file_handlers:
    print(handler)

randoms = [random.randrange(1, 10) for i in range(0, 200)]

commands = ["sleep %d && echo %d" % (j, i) for i, j in enumerate(randoms)]

processes = (Popen(cmd, shell=True) for cmd in commands)

running_processes = list(islice(processes, threads))

while running_processes:
    for i, process in enumerate(running_processes):
        if process.poll() is not None:
            out, err = process.communicate()
            file_handlers[i].write(out + "\n")
            running_processes[i] = next(processes, None)
            if running_processes[i] is None:
                del running_processes[i]
                break

for handler in file_handlers:
    handler.close()

