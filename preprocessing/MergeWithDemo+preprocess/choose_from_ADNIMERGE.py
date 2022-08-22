
import pandas as pd
import csv
def choose_from_ADNIMERGE():
    with open('data/ADNIMERGE.csv', "r"):
        reader1 = pd.read_csv('data/ADNIMERGE.csv', low_memory=False)

        data1 = reader1['RID']  # 获取name列的数据
        data2 = reader1['AGE']
        data3 = reader1['PTETHCAT']
        data4 = reader1['PTRACCAT']
        dataframe = pd.DataFrame({'RID': data1, 'AGE': data2, 'Ethnicity': data3, 'RACE': data4})

        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv("data/chosen_ADNIMERGE.csv", sep=',', index=False)