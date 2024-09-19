class ReversedList:
    def __init__(self, lst):
        self.lst = lst
    def __len__(self):
        return len(self.lst)
    def __getitem__(self, index):
        return self.lst[len(self.lst) - 1 - index]
rl = ReversedList([10, 23, 55])
for i in range(len(rl)):
    print(rl[i])