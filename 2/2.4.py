class MinStat:
    def __init__(self):
        self.number = []
    def add_number(self, num):
        self.number.append(num)
    def result(self):
        if len(self.number) == 0:
            return None
        return min(self.number)
class MaxStat:
    def __init__(self):
        self.number = []
    def add_number(self, num):
        self.number.append(num)
    def result(self):
        if len(self.number) == 0:
            return None
        return max(self.number)
class AverageStat:
    def __init__(self):
        self.number = []
    def add_number(self, num):
        self.number.append(num)
    def result(self):
        if len(self.number) == 0:
            return None
        return sum(self.number) / len(self.number)
values = [1, 0, 0]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))