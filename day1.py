# import pandas as pd

# # 创建列多层索引
# columns = pd.MultiIndex.from_tuples([('X', 'A'), ('X', 'B'), ('Y', 'C'), ('Y', 'D')])

# # 创建带有多层索引的DataFrame
# df = pd.DataFrame(data=[[1, 2, 3, 4]], columns=columns)
# print(df)


import pandas as pd

# 创建时间索引
time_index = pd.date_range('2023-01-01', periods=3, freq='D')
print(time_index)
# 创建多层索引
index = pd.MultiIndex.from_product([time_index, ['A', 'B']], names=['Time', 'Series'])
print(index)
# # 创建带有多层索引的DataFrame
df = pd.DataFrame(data=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], index=index, columns=pd.MultiIndex.from_product([['X', 'D'], ['Feature1', 'Feature2']]))
print(df)