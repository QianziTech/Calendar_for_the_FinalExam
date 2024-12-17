import pandas as pd
def to_csv(excelfile):
    excel=pd.read_excel(excelfile)
    excel.to_csv('output.csv',index=False)
excelfile="./demo/文件1734435028772.xlsx"
to_csv(excelfile)