
import modules.excel_hashing as excel_hashing
import pandas as pd
import tkinter as tk
from tkinter import ttk, filedialog

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

def create_ics_from_dataframe(df, filename):
    from icalendar import Calendar, Event,Alarm
    from datetime import datetime,timedelta
    import re
    
    cal = Calendar()
    for index,row in df.iterrows():
        event = Event()
        event.add('summary:'+'期末考试', row['课程名称'])
        date,time=row['考试时间'].split('(')
        start_time_str, end_time_str = time[:-1].split('-')
        start_datetime = datetime.strptime(date.strip() + ' ' + start_time_str.strip(), '%Y-%m-%d %H:%M')
        end_datetime = datetime.strptime(date.strip() + ' ' + end_time_str.strip(), '%Y-%m-%d %H:%M')
        event.add('dtstart', start_datetime)
        event.add('dtend', end_datetime)
        location=row['考试地点']   
        campus = get_campus(location)    
        event.add('location', campus+row['考试地点'])
        event.add('description', f"座号: {row['考试座号']}")      

                # 添加提醒，提前30分钟提醒
        alarm = Alarm()
        alarm.add('action', 'DISPLAY')
        alarm.add('description', '提醒: ' + row['课程名称'] + '期末考试')
        alarm.add('trigger', timedelta(minutes=-60))
        event.add_component(alarm)
  
        cal.add_component(event)

    
    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

def get_campus(location):
    import re
    from tkinter import filedialog
    match = re.match(r'(\d+)号楼', location)
    if match:
            building_number = match.group(1)
            if building_number in ['1', '2', '3', '4', '5', '6', '7', '8']:
                return '西校区'
            elif building_number in ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19','20','21']:
                return '中校区'
            elif building_number in ['22', '23', '24', '25', '26', '27', '28', '29', '30', '31','32',"33"]:
                return '东校区'
            else:
                return 'Unknown Campus'

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    excelfile = filedialog.askopenfilename(
        title="选择 Excel 文件",
        filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*"))
    )
    root.destroy()
    examlist=excel_hashing.to_csv(excelfile)
    print(examlist)
    columnlist=examlist.columns.values.tolist()
    quest=create_gui_for_column_selection(columnlist)
# 过滤出用户选择的列
    filtered_examlist = examlist[quest]
    print(filtered_examlist)
    # 生成 ICS 文件
    create_ics_from_dataframe(filtered_examlist, './result/output.ics')


