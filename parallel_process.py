#!/usr/bin/env python

import subprocess
from itertools import islice
import random

threads = 5

files = ["output.file%d" % i for i in range(0, threads)]

file_handlers = [None]*threads

for index, file_output in enumerate(files):
    file_handlers[index] = open(file_output, 'w')


randoms = [random.randrange(1, 10) for i in range(0, 200)]

commands = ["sleep %d && echo %d %d" % (j, i, j) for i, j in enumerate(randoms)]

processes = (subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
             for cmd in commands)

running_processes = list(islice(processes, threads))

while running_processes:
    for i, process in enumerate(running_processes):
        if process.poll() is not None:
            out, err = process.communicate()
            file_handlers[i].write(str(out) + "\n")
            running_processes[i] = next(processes, None)
            if running_processes[i] is None:
                del running_processes[i]
                break

for handler in file_handlers:
    handler.close()

