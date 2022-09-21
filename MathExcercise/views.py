import tkinter as tk
import practiceView


class ChoosePage:
    """generate choose operation page"""
    def __init__(self, root_page):
        self.root = root_page
        self.mode = tk.StringVar()
        self.mode.set(" + ")
        self.choose_frame = tk.Frame(self.root)
        self.generate_choose()

    def generate_choose(self):
        """generate  a page for choose one operation"""

        # choose operation
        tk.Label(self.choose_frame, text=" 请选择你要练习的运算：", font=("Arial", 20, "bold")).grid(row=1, column=1)

        # option
        tk.Radiobutton(self.choose_frame, text="+", variable=self.mode, value=" + ", font=("Arial", 20, "bold"))\
            .grid(row=1, column=2)
        tk.Radiobutton(self.choose_frame, text="-", variable=self.mode, value=" - ", font=("Arial", 20, "bold"))\
            .grid(row=2, column=2)
        tk.Radiobutton(self.choose_frame, text="*", variable=self.mode, value=" * ", font=("Arial", 20, "bold"))\
            .grid(row=3, column=2)
        tk.Radiobutton(self.choose_frame, text="/", variable=self.mode, value=" / ", font=("Arial", 20, "bold"))\
            .grid(row=4, column=2)

        # submit
        tk.Button(self.choose_frame,
                  text=" 确认并开始练习 ",
                  command=self.start_practise,
                  font=("Arial", 20, "bold"),
                  fg="red",
                  width=28,
                  pady=5,
                  ).grid(row=9, column=1, columnspan=2)

        self.choose_frame.place(relx=0.2, rely=0.2)

    def start_practise(self):
        """turn into next page"""
        self.choose_frame.destroy()
        practice = practiceView.Practice(self.root, self.mode.get())



