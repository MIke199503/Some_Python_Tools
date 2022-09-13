import tkinter as tk
from tkinter import messagebox, RIGHT, E
import pyperclip


class Tools:
    def __init__(self):
        """define a class to generate tool"""
        self.root = tk.Tk()
        self.root.title("蜡笔小新制作")
        self.root.geometry("+750+200")
        self.input_value = tk.StringVar()
        self.input_value.set(pyperclip.paste())
        self.result_value = tk.StringVar()
        self.mode = tk.IntVar()
        self.mode.set(2)
        self.builtScreen()
        self.root.mainloop()

    def builtScreen(self):
        """built basic GUI"""

        # row  - > 1 entry data
        # label for entry
        tk.Label(self.root, text="输入你的初始数据（如：5f9410或5ca2）：", justify=RIGHT, anchor=E).grid(row=1, column=2)

        # entry
        tk.Entry(self.root,
                 textvariable=self.input_value,
                 validate="focusout",
                 validatecommand=self.check_len,
                 invalidcommand=messagebox.showinfo(title="输入有误",
                                                    message="长度要求 < 6 \n 没有设置很多错误检测，请按规矩来！！")).grid(row=1, column=3)

        # row - > 2 choose mode
        tk.Label(self.root, text="请选择你需要执行的模式：", justify=RIGHT, anchor=E).grid(row=2, column=2)

        # mode options
        tk.Radiobutton(self.root, text="565 To 888", variable=self.mode, value=1).grid(row=3, column=3)
        tk.Radiobutton(self.root, text="888 To 565", variable=self.mode, value=2).grid(row=2, column=3)

        # row - > 3 run it
        tk.Button(self.root,
                  text="Run",
                  command=self.get_result,
                  width=30,
                  fg="red",
                  ).grid(row=4, columnspan=3, column=1)

        # row - > 4 results
        tk.Label(self.root, text="结果:").grid(row=5, column=2)
        result = tk.Label(self.root, textvariable=self.result_value, relief=tk.SUNKEN, width=20)
        result.bind("<Button-1>", self.bind_callback)
        result.grid(row=5, column=3)

    def bind_callback(self, event):
        pyperclip.copy(self.result_value.get())

    def get_result(self):
        """get result/mode"""
        mode = self.mode.get()
        if mode == 1:
            answer = messagebox.askokcancel(title="警告", message='RGB565 转 RGB888 缺失数据由0补全，因此色彩会发生细微变化')
            if answer:
                self.result_value.set(self.r5tr8(self.input_value.get()))
        else:
            self.result_value.set(self.r8tr5(self.input_value.get()))

    def check_len(self):
        """check the length of the entry """
        if len(self.input_value.get()) > 7:
            return False
        else:
            return True

    def r8tr5(self, string):
        """ convert rgb888(24) to rgb555(16)"""
        string_to_binary = "{:024b}".format(int(string, 16))
        red5 = string_to_binary[0:8][0:5]
        green5 = string_to_binary[8:16][0:6]
        black5 = string_to_binary[16:24][0:5]
        return hex(int((red5+green5+black5), 2))[2:]

    def r5tr8(self, string):
        """convert rgb555(16) to rgb888(24),Use zeros for complement"""
        string_to_binary = "{:016b}".format(int(string, 16))
        red8 = string_to_binary[0:5]+"0"*3
        green8 = string_to_binary[5:11] + "0"*2
        black8 = string_to_binary[11:16] + "0"*3
        return hex(int((red8+green8+black8), 2))[2:]


if __name__ == '__main__':
    a = Tools()

