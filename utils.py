def create_2d_list(rows, cols, default=0): ## creates [rows+1], [cols+1] 2D list for matrix frame
    return [[(default() if callable(default) else default) for i in range(int(rows)+1)] for j in range(int(cols)+1)]

def get_screen_geometry(root, divider=1):
    root.update_idletasks()
    screen_width = str(root.winfo_screenwidth()//divider)
    screen_height = str(root.winfo_screenheight()//divider)
    return screen_width + "x" + screen_height
