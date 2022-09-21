import time
import tkinter as tk
import topic
from tkinter import messagebox
import ErrorView


class Practice:
    """practice page"""
    def __init__(self, root_page, operation):
        # base information
        self.operation = operation
        self.root = root_page

        # the entry result variable
        self.entry_result = tk.StringVar()
        self.entry_result.set(0)

        # process information
        self.process = 0
        self.process_string = tk.StringVar()
        self.process_string.set(str(self.process) + " / 20")
        self.process_frame = tk.Frame(self.root)
        self.process_frame.place(relx=0.0, rely=0.0)
        tk.Label(self.process_frame, textvariable=self.process_string).pack()

        # the first built practice views
        self.practice_frame = tk.Frame(self.root, relief=tk.RIDGE)
        self.practice_frame.place(relx=0.2, rely=0.2)

        # get topic data
        self.num_a, self.num_b, self.answer = topic.get_single_item(self.operation)

        # set numa numb
        self.numa = tk.IntVar()
        self.numa.set(self.num_a)
        self.numb = tk.IntVar()
        self.numb.set(self.num_b)

        self.generate_practice()

    def generate_practice(self):
        """generate practice detail """

        # numa
        tk.Label(self.practice_frame,
                 textvariable=self.numa,
                 font=("Arial", 20, "bold"),
                 anchor='w').grid(row=2, column=2)

        # operation
        tk.Label(self.practice_frame,
                 textvariable=self.numb,
                 font=("Arial", 20, "bold"),
                 anchor='w').grid(row=3, column=2)

        # numb
        tk.Label(self.practice_frame,
                 text=self.operation,
                 font=("Arial", 30, "bold"),
                 fg="red",
                 anchor='e').grid(row=3, column=1)

        # underline
        my_canvas = tk.Canvas(self.practice_frame, width=300, height=22)
        my_canvas.create_line(0, 0, 300, 0, width=20, fill='black')
        my_canvas.grid(row=4, column=1, columnspan=2)

        # answer entry
        tk.Entry(self.practice_frame,
                 textvariable=self.entry_result,
                 validate="focusout",
                 font=("Arial", 20, "bold"),
                 relief=tk.RIDGE,
                 ).grid(row=5, column=2)
        # answer label
        tk.Label(self.practice_frame,
                 text="请输入结果",
                 font=("Arial", 20, "normal"),
                 anchor='w').grid(row=5, column=1)

        # placeholder
        tk.Label(self.practice_frame,
                 text=" ",
                 height=5).grid(row=6, column=1)

        # get next item button
        tk.Button(self.practice_frame,
                  text=" 下一题 ",
                  command=self.get_next_item,
                  font=("Arial", 20, "bold"),
                  fg="red",
                  width=10,
                  pady=5,
                  ).grid(row=7, column=2)

    def get_next_item(self):
        """set next practice data """
        # if  answer is right ?
        if self.entry_result.get() == str(self.answer):
            # clear entry
            self.entry_result.set("")

            # process grow
            self.process += 1
            self.process_string.set(str(self.process) + " / 20")

            # if 20 finish
            if self.process < 20:
                # update topic data
                self.num_a, self.num_b, self.answer = topic.get_single_item(self.operation)
                # flash
                self.numa.set(self.num_a)
                self.numb.set(self.num_b)
            else:
                # practice done
                if messagebox.showinfo(title="今日通关完成！", message="今日20题练习结束"):
                    self.root.quit()
        else:
            # enter error view
            ErrorView.ErrorView(root_page=self.root, operation=self.operation)
