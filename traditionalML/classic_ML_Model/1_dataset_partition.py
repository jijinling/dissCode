import pandas as pd
import numpy as np

#data=pd.read_csv('./data/1/demographic_with_volumn_new.csv')
data=pd.read_csv('./data/2/demographic_with_volumn_with_area_new.csv')
data_0=data.loc[data['label'] == 0]
data_1=data.loc[data['label'] == 1]

proportion=0.8  #divide the proportion  8:2

shuffled_inde0 = np.random.permutation(len(data_0))
split_inde0 = int(len(data_0)*proportion)
train_inde0 = shuffled_inde0[:split_inde0]
test_inde0 = shuffled_inde0[split_inde0:]
train_0 = data_0.iloc[train_inde0, :]
test_0 = data_0.iloc[test_inde0, :]

shuffled_inde1 = np.random.permutation(len(data_1))
split_inde1 = int(len(data_1)*proportion)
train_inde1 = shuffled_inde1[:split_inde1]
test_inde1 = shuffled_inde1[split_inde1:]
train_1 = data_1.iloc[train_inde1, :]
test_1 = data_1.iloc[test_inde1, :]


train = pd.concat([train_0,train_1])
test  = pd.concat([test_0,test_1])


# train.to_csv('./data/1/train.csv', index=False, encoding='utf-8-sig')
# test.to_csv('./data/1/test.csv', index=False, encoding='utf-8-sig')

train.to_csv('./data/2/train.csv', index=False, encoding='utf-8-sig')
test.to_csv('./data/2/test.csv', index=False, encoding='utf-8-sig')


