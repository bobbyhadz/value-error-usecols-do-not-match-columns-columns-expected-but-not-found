# Usecols do not match columns, columns expected but not found 

import pandas as pd

df = pd.read_csv(
    'employees.csv',
    sep=',',
    encoding='utf-8',
    usecols=['first_name', 'date']
)

#   first_name        date
# 0      Alice  2023-01-05
# 1      Bobby  2023-03-25
# 2       Carl  2021-01-24
print(df)
