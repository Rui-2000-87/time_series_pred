# -*- coding=utf-8-*- 

class AverageMeter(object):
    def __init__(self, trunc, trunc_num):
        self.reset()
        self.trunc = trunc
        self.trunc_num = trunc_num
        if trunc:
            self.history_data = []

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        if self.trunc:
            self.history_data.extend([val]*n)
            if len(self.history_data) > self.trunc_num:
                self.history_data = self.history_data[-self.trunc_num:]
            self.sum = sum(self.history_data)
            self.count += n
            self.avg = self.sum / len(self.history_data)
        else:
            self.val = val
            self.sum += val * n
            self.count += n
            self.avg = self.sum / self.count