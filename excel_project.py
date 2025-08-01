import os
import pandas as pd
from excel_tren import WorkwithFiles
from math_class import DiagrammDraw
def inputf(str,default):
    i=input(str)
    if not i:
        i = default
    return i
list=os.listdir()
files=[]
config=pd.read_json("config.json").head(0)
for file in list:
    if file.endswith(".xlsx"):
        df=pd.read_excel(file).head(0)
        if config.equals(df):
            files.append(file)
            print(f"{file} добавлен")
fl=WorkwithFiles()
h=inputf("категори по каторой будет проходит группировка","Категория")
g=inputf("что суммируем","Сумма")
files_sum=[]
a=0
for file in files:
    df=pd.read_excel(file)
    i=inputf("название файла",str(a))
    fl.group_and_sum("сумма",df,i,[h,g])
    dia=DiagrammDraw()
    ia=inputf("название листа с данными ","Sheet1")
    dia.diagramm(f"{i}.xlsx",ia)
    a=a+1
    
