import tkinter as tk
from tkinter import messagebox
import utils
from PIL import Image, ImageTk
from matrix_class import matrix

class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.matrixes = []
        self.totalCol = 0
        self.init_widgets()

    def init_widgets(self):

        self.img_canvas = tk.Canvas(self, width = 320, height = 200)
        self.img_canvas.pack()
        self.img = ImageTk.PhotoImage(file="keanu_ps1.jpg")
        self.img_canvas.create_image(0,0,anchor="nw", image=self.img)

        self.transpose_button = tk.Button(self, text="get transpose of a matrix", command=self.show_transpose_menu)
        self.transpose_button.pack(side="top")

        self.canvas = tk.Canvas(self, bg="blue", width = 400, height = 400)
        self.canvas.pack()


    def update_rows_cols(self, A):
        self.totalCol -= A.col_count
        A.resize(int(A.row_var.get()), int(A.col_var.get()))
        self.totalCol += A.col_count

    def construct_matrix_input(self, letter, default_rows, default_cols):

        temp = matrix(letter, default_rows, default_cols)

        ## create basic row/col number input & data row/col input
        temp.row_var, temp.col_var = tk.StringVar(value=default_rows), tk.StringVar(value=default_cols)

        temp.row_label = tk.Label(self, text="nr of rows: ")
        temp.row_entry = tk.Entry(self, textvariable=temp.row_var, width=2)

        temp.col_label = tk.Label(self, text="nr of cols: ")
        temp.col_entry = tk.Entry(self, textvariable=temp.row_var, width=2)

        temp.data_entry_var = utils.create_2d_list(temp.row_count, temp.col_count, lambda: tk.StringVar(value=0))
        temp.data_entry = utils.create_2d_list(temp.row_count, temp.col_count, 0)

        for i in range(1, temp.row_count+1):
            for j in range(1, temp.col_count+1):
                temp.data_entry[i][j] = tk.Entry(self, textvariable=temp.data_entry_var[i][j], width=2)


        self.matrixes.append(temp)
        crt = self.matrixes[-1]
        crt.size_upd_button = tk.Button(self, text="update matrix " + letter + " size", command = lambda: self.update_rows_cols(crt))
        crt.get_transp_button = tk.Button(self, text="get transpose of " + letter, command = lambda: self.get_transpose(crt))
        ##
        ## when updating matrix size, input below should change (+ move other matrixes down!!)
        ## plot widgets
        self.canvas.create_window(50, 25, window=crt.row_label)
        self.canvas.create_window(100, 25, window=crt.row_entry)
        self.canvas.create_window(150, 25, window=crt.col_label)
        self.canvas.create_window(200, 25, window=crt.col_entry)
        self.canvas.create_window(275, 25, window=crt.size_upd_button)
        ##
        ## plot row/col data input.
        #print(crt.data_entry[1][1], crt.data_entry[2][1])
        '''self.canvas.create_window(40, 75, window=crt.data_entry[1][1])
        self.canvas.create_window(70, 75, window=crt.data_entry[1][2])
        self.canvas.create_window(100, 120, window=crt.data_entry[2][1])'''
        print(temp.data_entry)
        for i in range(1, crt.row_count+1):
            for j in range(1, crt.col_count+1):
                col_modifier = (j-1) * 25
                row_modifier = (i-1) * 25
                print(col_modifier, row_modifier)
                self.canvas.create_window(40+row_modifier, 75+col_modifier, window=crt.data_entry[i][j])

        self.canvas.create_window(75, 75 +(crt.col_count+1) * 25, window=crt.get_transp_button)


    def get_transpose(self, mat):
        mat.update_values()
        msg = "A transpose:\n"
        for i in range(1, mat.col_count+1):
            for j in range(1, mat.row_count+1):
                msg += str(mat.M[i][j]) + " "
            msg += "\n"

        messagebox.showinfo("Matrix Transpose", msg)
    def show_transpose_menu(self):
        self.construct_matrix_input("A", "2", "2")




root = tk.Tk()
root.geometry(utils.get_screen_geometry(root))
root.title("matrix manipulator")

window = app(master=root)
window.mainloop()
