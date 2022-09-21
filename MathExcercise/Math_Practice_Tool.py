import tkinter as tk
import views


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x400+700+140")
    root.title("每日20题.By.爸爸给乖女儿的爱的礼物")
    choose_page = views.ChoosePage(root_page=root)
    root.mainloop()
