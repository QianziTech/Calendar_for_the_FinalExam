
import modules.excel_hashing as excel_hashing
import pandas as pd
import tkinter as tk
from tkinter import ttk

def create_gui_for_column_selection(columns):
    def on_submit():
        selected_columns.set([columns[i] for i in range(len(columns)) if var_list[i].get()])
        root.quit()

    root = tk.Tk()
    root.title("选择需要使用的列")

    label = tk.Label(root, text="请选择需要使用的列：")
    label.pack()

    var_list = []
    for col in columns:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(root, text=col, variable=var)
        chk.pack(anchor='w')
        var_list.append(var)

    submit_button = tk.Button(root, text="提交", command=on_submit)
    submit_button.pack()

    selected_columns = tk.Variable()
    root.wait_variable(selected_columns)
    root.destroy()
    return list(selected_columns.get())

if __name__ == "__main__":
    excelfile="demo/文件1734435028772.xlsx"
    examlist=excel_hashing.to_csv(excelfile)
    print(examlist)
    columnlist=examlist.columns.values.tolist()
    quest=create_gui_for_column_selection(columnlist)
    print(list(quest))
    quest_column=["课程名称","考试时间","考试地点","考试座号"]
