import pandas as pd
import os
def to_csv(excelfile):
    excel=pd.read_excel(excelfile)
    output_dir = './output'
    if not(os.path.exists(output_dir)):
        os.makedirs(output_dir)
    excel.to_csv('./output/output.csv',index=False)
    return pd.read_csv('./output/output.csv')
