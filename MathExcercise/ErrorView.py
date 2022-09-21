import tkinter as tk
import topic


class ErrorView:
    def __init__(self, root_page, operation):
        """ use for error practice """

        # basic information
        self.root = root_page
        self.operation = operation

        # basic_white to cover practice views
        self.basic_white = tk.Frame(self.root, background="WHITE")
        self.basic_white.pack(fill='both', expand="yes")

        #  base_frame to show 5 topic
        self.base_frame = tk.Frame(self.basic_white)
        self.base_frame.pack(expand='yes')

        # get error item
        self.num_list = topic.get_five_error_item(self.operation)

        # resource for get 5 entry result
        self.resource = []
        for x in range(5):
            self.resource.append(tk.StringVar())

        # generate error view detail
        self.generate(self.num_list)

    def generate(self, num_list):
        """built topic rows """
        for index in range(len(num_list)):
            self.row(base_page=self.base_frame, x=num_list[index][0], y=num_list[index][1], row=index + 1, final=len(num_list)+1)

    def check_item(self):
        """check the entry result is right  """
        # flag for no one is wrong
        flag = True

        # check result
        for x in range(len(self.resource)):
            if self.resource[x].get() == str(self.num_list[x][2]):
                pass
            else:
                flag = False
                # print(f"第{x + 1}题错误")
        # anyone is wrong
        if not flag:
            # do again
            self.re_built()
        else:
            # no on is wrong , delete this page
            self.base_frame.destroy()
            self.basic_white.destroy()

    def row(self, base_page, x, y, row, final):
        """ built one row detail """

        # numa
        tk.Label(base_page,
                 text=x,
                 font=("Arial", 20, "bold")).grid(row=row, column=1)

        # operation
        tk.Label(base_page,
                 text=self.operation,
                 font=("Arial", 20, "bold")).grid(row=row, column=2)

        # numb
        tk.Label(base_page,
                 text=y,
                 font=("Arial", 20, "bold")).grid(row=row, column=3)

        # equal
        tk.Label(base_page,
                 text="=",
                 font=("Arial", 20, "bold")).grid(row=row, column=4)

        # result entry
        tk.Entry(base_page,
                 textvariable=self.resource[row-1],
                 font=("Arial", 20, "bold")).grid(row=row, column=5)

        # placeholder
        tk.Label(base_page,
                 text=" ",
                 font=("Arial", 30, "bold")).grid(row=final, column=0)

        # submit button
        tk.Button(base_page,
                  text="提交",
                  command=self.check_item,
                  width=30,
                  foreground='red',
                  font=("Arial", 20, "bold")).grid(row=final+1, column=1, columnspan=5)

    def re_built(self):
        """do again fresh view """

        # delete old view
        self.base_frame.destroy()

        # get a new views
        self.base_frame = tk.Frame(self.basic_white)
        self.base_frame.pack(expand='yes')

        # get new data
        self.num_list = topic.get_five_error_item(self.operation)

        self.resource = []
        for x in range(5):
            self.resource.append(tk.StringVar())

        self.generate(self.num_list)


