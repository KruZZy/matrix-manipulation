import utils

class matrix(object):
    def __init__(self, letter, row_count, col_count):
        self.letter = letter
        self.row_count, self.col_count = int(row_count), int(col_count)
        self.M = utils.create_2d_list(row_count, col_count)

    def resize(self, row_count, col_count):
        ## when resizing, original submatrix should be remembered.
        temp = utils.create_2d_list(row_count, col_count)
        for i in range(1, min(self.row_count, row_count)+1):
            for j in range(1, min(self.row_count, row_count)+1):
                    temp[i][j] = self.M[i][j]

        self.M = temp
        self.row_count, self.col_count = row_count, col_count

    def update_values(self):
        for i in range(1, self.row_count+1):
            for j in range(1, self.col_count+1):
                self.M[i][j] = int(self.data_entry_var[i][j].get())
