from tkinter import *
from PIL import Image, ImageTk
class Board(Canvas):
    def __init__(self, parent, square_size=160):
        super().__init__(parent, width=9 * square_size, height=10 * square_size,
                         background="#DDB88C")

        # 设置棋盘的宽度和高度
        self.square_size = square_size
        self.width = 9 * square_size
        self.height = 10 * square_size

        # load the board image
        self.board_image = ImageTk.PhotoImage(Image.open(
            "C:\\Users\\陈\\PycharmProjects\\中国象棋\\images\\棋盘.png"))
        self.create_image(0, 0, anchor=NW, image=self.board_image)

        # 计算棋盘的左上角位置，使其在窗口中居中显示
        x = (parent.winfo_width() - self.width) // 2
        y = (parent.winfo_height() - self.height) // 2
        self.place(x=x, y=y)
        # load the piece images
        self.piece_images = {}
        self.load_piece_images()
        # create the board setup
        self.board = [
            ['车', '马', '相', '士', '帅', '士', '相', '马', '车'],
            ['', '', '', '', '', '', '', '', ''],
            ['', '炮', '', '', '', '', '', '炮', ''],
            ['兵', '', '兵', '', '兵', '', '兵', '', '兵'],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['卒', '', '卒', '', '卒', '', '卒', '', '卒'],
            ['', '砲', '', '', '', '', '', '砲', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['車', '馬', '象', '仕', '将', '仕', '象', '馬', '車']
        ]
        self.draw_board()
        # Create reset button
        self.reset_button = Button(parent, text="Reset",
                                   command=self.reset_board)
        self.reset_button.place(x=2000, y=50)
        self.reset_button.configure(width=10, height=2)
    def draw_board(self):
        for row, columns in enumerate(self.board):
            for column, piece in enumerate(columns):
                if piece != '':
                    x, y = self.get_coords(row, column)
                    self.create_image(x, y, anchor=CENTER,
                                      image=self.piece_images[piece])
    def draw_piece(self, row, col, piece):
        if piece is None:
            return
        image = self.piece_images[piece]
        x = col * self.square_size + self.square_size/2
        y = row * self.square_size + self.square_size
        self.canvas.create_image(x, y, image=image, anchor='nw')
    def reset_board(self):
        self.delete("all")
        self.draw_board()

    def get_coords(self, row, column):
        x = (column * self.square_size) + int(self.square_size / 2)
        y = (9 - row) * self.square_size + int(self.square_size / 2)
        return x, y

    def load_piece_images(self):
        for piece in ['車', '馬', '象', '士', '将', '炮', '兵', '卒', '砲', '相',
                      '仕', '帅', '车', '马']:

            image_file = f"C:\\Users\\陈\\PycharmProjects\\中国象棋\\图片2\\{piece}.png"
            image = Image.open(image_file)
            size = (int(self.square_size / 1.1), int(self.square_size / 1.1))
            image = image.resize(size, Image.ANTIALIAS)
            self.piece_images[piece] = ImageTk.PhotoImage(image)

root = Tk()
root.title("中国象棋")
root.state('zoomed')
board = Board(root, square_size=120)
board.pack()
root.mainloop()