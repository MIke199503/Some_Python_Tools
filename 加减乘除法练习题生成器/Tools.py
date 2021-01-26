'''
Author: your name
Date: 2021-01-25 18:50:44
LastEditTime: 2021-01-25 22:07:15
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/Users/zhutaohe/Downloads/Tools.py
'''
import tkinter
import tkinter.messagebox
import random

class Window:
        def __init__(self):

                #基础数据[
                self.data_range_tuple = (10,20,30,40,50,60,70,80,90,100,1000)

                #主窗口创建
                self.root = tkinter.Tk()
                self.root.title("加减乘除练习题生成器")
                
                #布局基础界面
                self.set_up()

                #界面保持
                tkinter.mainloop()



        def set_up(self):
                #复选框动态变量
                self.add = tkinter.IntVar()
                self.sub = tkinter.IntVar()
                self.plus = tkinter.IntVar()
                self.divi = tkinter.IntVar()
                self.data_range = tkinter.IntVar()      #数据范围
                self.data_count = tkinter.IntVar()     #需要多少项数据
                self.minus_sign_ok = tkinter.IntVar() #是否考虑负号
                
                #提示label1
                label_one = tkinter.Label(self.root,text = "请选择你想要添加的运算法则：" , fg= "blue",font= ("Arial",20,"bold"))
                label_one.grid(row =0,column = 0,padx=10, pady=5)

                #加减乘除复选框
                add_check = tkinter.Checkbutton(self.root,text = "加法运算：+ ",variable = self.add,fg= "blue",font= ("Arial",18,"normal"))
                sub_check = tkinter.Checkbutton(self.root,text = "减法运算: - ",variable = self.sub,fg= "blue",font= ("Arial",18,"normal"))
                plus_check = tkinter.Checkbutton(self.root,text = "乘法运算: * ",variable = self.plus,fg= "blue",font= ("Arial",18,"normal"))
                divi_check = tkinter.Checkbutton(self.root,text = "除法运算: \\ ",variable = self.divi,fg= "blue",font= ("Arial",18,"normal"))
                add_check.grid(row=0,column = 1,padx=10, pady=5)
                sub_check.grid(row=1,column = 1,padx=10, pady=5)
                plus_check.grid(row=2,column = 1,padx=10, pady=5)
                divi_check.grid(row=3,column = 1,padx=10, pady=5)

                #提示label2
                label_two = tkinter.Label(self.root,text = "请选择你需要随机的数据范围：" , fg= "blue",font= ("Arial",20,"bold"))
                label_two.grid(row =4,column = 0,padx=10, pady=5)

                #数据范围：
                spin_one = tkinter.Spinbox(self.root,values = self.data_range_tuple,textvariable = self.data_range,command = self.data_check,fg= "blue",font= ("Arial",18,"normal"))
                spin_one.grid(row = 4,column = 1,padx=10, pady=5)

                #提示label3
                label_three = tkinter.Label(self.root,text = "请选择你需要随机多少项数据：" , fg= "blue",font= ("Arial",20,"bold"))
                label_three.grid(row =5,column = 0,padx=10, pady=5)

                #数据项数
                self.test = self.root.register(self.count_check)
                self.count  = tkinter.Entry(self.root,textvariable = self.data_count,validate = "focusout",fg= "blue",font= ("Arial",18,"normal"),validatecommand = (self.test,"%P"),invalidcommand = self.check_error)
                self.count.grid(row =5,column = 1,padx=10, pady=5)

                #提示label4
                label_three = tkinter.Label(self.root,text = "请选择你是否排除负号的情况：" , fg= "blue",font= ("Arial",20,"bold"))
                label_three.grid(row =6,column = 0,padx=10, pady=5)
                
                #在意负号
                minus_sign = tkinter.Radiobutton(self.root,text = "考虑",variable = self.minus_sign_ok,value = 0 )
                minus_sign.grid(row = 6,column = 1,padx = 10, pady = 5)
                
                #不在意负号
                minus_sign_no = tkinter.Radiobutton(self.root,text = "不考虑",variable = self.minus_sign_ok,value = 1 )
                minus_sign_no.grid(row = 6,column = 2,padx = 10, pady = 5)

                #生成数据按钮
                result_button = tkinter.Button(self.root,text = "生成表格",fg= "red",font= ("Arial",20,"bold"),width = 25,command = self.click_button)
                result_button.grid(row = 7,padx = 10, pady = 5)

        #按钮响应
        def click_button(self):
                
                if self.add.get() == 0 and self.sub.get() == 0 and self.plus.get() == 0  and self.divi.get() == 0 :
                        tkinter.messagebox.showerror("不正确的选择","请至少选择一项运算！")
                else:
                        res = self.result()
                        for i in range(len(res[0])):
                                print(str(res[0][i]) + res[1][i] + str(res[2][i]) + "="  )
        
        #测试
        def data_check(self):
                print(self.data_range.get())

        #项目数输入验证
        def count_check(self,content):
                if content.isdigit():
                        print(self.data_count.get())
                        return True
                else:
                        return False
        #输入错误提醒及清空
        def check_error(self):
                tkinter.messagebox.showerror('错误','请输入正确的项目数！！')
                self.count.delete(0,'end')

        #产出数据
        def result(self):
                resultlist = [[],[],[]] #结果数据列表

                #转换数据
                data_fanwei = self.data_range.get()
                data_geshu = self.data_count.get()
                minus_ok = self.minus_sign_ok.get()
                
                #收集需要的运算
                operation = []
                if self.add.get() == 1 :
                        operation.append("+")
                if self.sub.get() == 1 :
                        operation.append("-")
                if self.plus.get() == 1:
                        operation.append("*")
                if self.divi.get() == 1 :
                        operation.append("\\")
                        
                #不考虑负号的情况
                if minus_ok == 1:
                       for i in range(0,data_geshu):
                                resultlist[0].append(random.randint(-data_fanwei,data_fanwei))
                                a = random.choice(operation)
                                resultlist[1].append(a)
                                #排除除数为0的问题
                                if a == "\\":
                                        num_1 = random.choice([random.randint(-data_fanwei,-1),random.randint(1,data_fanwei)])
                                        resultlist[2].append(num_1)
                                else:
                                        resultlist[2].append(random.randint(-data_fanwei,data_fanwei))
                else:
                        for i in range(0,data_geshu):
                                resultlist[0].append(random.randint(0,data_fanwei))
                                a = random.choice(operation)
                                resultlist[1].append(a)
                                #筛选相减为负的情况
                                if a == "-":
                                        resultlist[2].append(random.randint(0,resultlist[0][i]))
                                #排除被除数为0的情况
                                elif a == "\\":
                                        resultlist[2].append(random.randint(1,data_fanwei))
                                else:
                                        resultlist[2].append(random.randint(0,data_fanwei))

                return resultlist



class ExcelWork():
        pass    


if __name__ == "__main__":
        win = Window()




