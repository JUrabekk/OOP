class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day
    def __sub__(self, other):
        res = (self.month - other.month) * 30 + (self.day - other.day)
        return res
mar5 = Date(3, 1)
jan1 = Date(1, 1)
print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)