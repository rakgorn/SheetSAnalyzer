import openpyxl as op
from openpyxl.chart import BarChart,Reference

class DiagrammDraw():
    def diagramm(self,excel_file,i):
            df=op.load_workbook(excel_file)
            source=df[i]

            chart_sheet=df.create_sheet('Диаграмма')
            chart=BarChart()
            chart.title='Расходы'
            chart.x_axis.title='Расходы'
            chart.y_axis.title='Рубли'
            data = Reference(source, min_col=1,max_col=10, min_row=1,max_row=10)
            chart.add_data(data,titles_from_data=True)
            chart_sheet.add_chart(chart, "A1")     
            df.save(excel_file)