
import time
import os

def logger(exp_path, exp_name):
    from tensorboardx import SummaryWriter

    if not os.path.exists(exp_path):
        os.mkdir(exp_path)

    writer = SummaryWriter(exp_path + "/" + exp_name)

    return writer


class Timer:

    def __init__(self):
        self.start_time = 0.
        self.total_time = 0.
        self.calls = 0
        self.diff = 0.
        self.average_time = 0.

    def tic(self):
        self.start_time = time.time()

    def toc(self):
        self.diff = time.time() - self.start_time
        self.total_time += self.diff
        self.calls += 1
        self.average_time = self.total_time / self.calls
        if average:
            return self.average_time
        else:
            return self.diff
