import pandas as pd
def to_csv(excelfile):
    excel=pd.read_excel(excelfile)
    excel.to_csv('./output/output.csv',index=False)
    return pd.read_csv('./output/output.csv')
