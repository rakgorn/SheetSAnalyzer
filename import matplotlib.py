import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 30]

plt.bar(labels, values, color='skyblue')
plt.title("Столбчатая диаграмма")
plt.xlabel("Категории")
plt.ylabel("Значения")
plt.show()
