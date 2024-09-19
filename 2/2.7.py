class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            return None
    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
    def n_rows(self):
        return self.rows
    def n_cols(self):
        return self.cols
    def delete_row(self, row):
        if 0 <= row < self.rows:
            del self.data[row]
            self.rows -= 1
    def delete_col(self, col):
        if 0 <= col < self.cols:
            for row in self.data:
                del row[col]
            self.cols -= 1
    def add_row(self, row):
        if row >= self.rows:
            self.rows = row + 1
        new_row = [0 for _ in range(self.cols)]
        self.data.insert(row, new_row)
    def add_col(self, col):
        if col >= self.cols:
            self.cols = col + 1
        for row in self.data:
            row.insert(col, 0)
tab = Table(2, 2)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
tab.add_row(0)
tab.add_col(1)
for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()