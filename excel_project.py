import os
import pandas as pd
from excel_tren import WorkwithFiles
from math_class import DiagrammDraw
def inputf(str,default):
    i=input(str)
    if not i:
        i = default
    return i
work_with_file=WorkwithFiles()
diagramm=DiagrammDraw()
list=os.listdir()
files=[]
config=pd.read_json("config.json").head(0)
for file in list:
    if file.endswith(".xlsx"):
        df=pd.read_excel(file).head(0)
        if config.equals(df):
            files.append(file)
            print(f"{file} добавлен")
group_col=inputf("категори по каторой будет проходит группировка","Категория")
sum_col=inputf("что суммируем","Сумма")
a = 0
sheet_name=inputf("название листа с данными ","Sheet1")
for file in files:
    df = pd.read_excel(file)

    base_name = os.path.splitext(file)[0]          # 'Иванов' из 'Иванов.xlsx'
    default_name = f"{a}_{base_name}"              # например, '0_Иванов'
    file_name = inputf("Название выходного файла: ", default_name)

    # Проверка на дублирование расширения
    if not file_name.endswith(".xlsx"):
        file_name += ".xlsx"

    # Группировка и сохранение
    work_with_file.group_and_sum(df, file_name, [group_col, sum_col])

    # Построение диаграммы
    diagramm.diagramm(file_name, sheet_name)

    a += 1