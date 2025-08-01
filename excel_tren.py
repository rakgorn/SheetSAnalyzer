class WorkwithFiles():     
    def group_and_sum(self, df, name, cols):   
        if not isinstance(cols, list) or len(cols) != 2:
            raise ValueError("cols должен быть списком из двух элементов: [группировка, сумма]")

        for col in cols:
            if col not in df.columns:
                raise KeyError(f"Колонка '{col}' не найдена в DataFrame")

        group_col, sum_col = cols
        grouped = df.groupby(group_col, as_index=False)[sum_col].sum()

        if not name.endswith('.xlsx'):
            name += '.xlsx'

        grouped.to_excel(name, index=False)


    
        