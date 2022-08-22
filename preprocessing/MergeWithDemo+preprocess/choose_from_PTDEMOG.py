import pandas as pd
import csv
def choose_from_PTDEMOG():
    with open('data/PTDEMOG.csv', "r"):
        reader1 = pd.read_csv('data/PTDEMOG.csv', low_memory=False)

        data1 = reader1['ID']  # 获取name列的数据
        data2 = reader1['RID']
        data3 = reader1['PTGENDER']
        data4 = reader1['PTHAND']
        data5 = reader1['PTMARRY']
        data6 = reader1['PTEDUCAT']
        data7 = reader1['PTWORK']
        data8 = reader1['PTWRECNT']
        data9 = reader1['PTHOME']
        data10 = reader1['PTPLANG']
        dataframe = pd.DataFrame({'ID': data1, 'RID': data2, 'GENDER': data3, 'HAND': data4, 'MARRY': data5, 'PTEDUCAT': data6, 'PTWORK': data7, 'PTWRECNT': data8, 'PTHOME': data9, 'PTPLANG': data10})

        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv("data/chosen_PTDEMOG.csv", sep=',', index=False)