import pandas as pd

# data = {
#     'Набор А': [85, 90, 95, 100, 105],
#     'Набор Б': [70, 80, 95, 110, 120],
# }
#
# df = pd.DataFrame(data)

# stdA = df['Набор А'].std()
# stdB = df['Набор Б'].std()
#
# print(f"Стандартное отклонение для набора А: {stdA}")
# print(f"Стандартное отклонение для набора Б: {stdB}")

data = {
    'Возраст': [23, 25, 27, 28, 21, 22, 24, 26, 29, 22],
    'Зарплата': [54000, 50800, 52000, 55000, 50000, 56000, 52000, 58000, 49000, 50110],
}

df = pd.DataFrame(data)