import os
import pandas as pd
import openpyxl

class WorkwithFiles():
    def combine(self,files,df_str):
        df=pd.DataFrame()
        for file in files:
            if file.endswith(".xlsx") and file !=df_str:
                fl=pd.read_excel(file)
                df=pd.concat([df,fl],ignore_index=True)
                print(file,"complete")
        return df        
    def group_and_sum(self,category,fg,name,a):
        config=pd.read_json("config.json").head(0)    
        grouped = fg.groupby(a[0], as_index=False)[a[1]].sum()
        grouped.to_excel(name+'.xlsx', index=False)

    
        