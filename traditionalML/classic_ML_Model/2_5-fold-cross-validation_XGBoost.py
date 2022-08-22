import numpy as np
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier


def Model_tmp(data1,info1):
    val_score_list=[]
    folds = KFold(n_splits=5, shuffle=True, random_state=1)
    val_score_best=0
    for train_index, test_index in folds.split(data1):  # callsplit() to split data
        X_train  = data1.iloc[train_index,:]
        X_val = data1.iloc[test_index,:]

        train_label = info1.iloc[train_index,:]
        val_label = info1.iloc[test_index, :]


        y_train = train_label.values.ravel()
        y_val = val_label.values.ravel()

        param_test1 = {
            'max_depth': list(range(3, 10, 2)),
            'min_child_weight': list(range(1, 6, 2)),
            'gamma': [i / 10.0 for i in range(0, 5)],
            'subsample': [i / 100.0 for i in range(75, 90, 5)],
            'colsample_bytree': [i / 100.0 for i in range(75, 90, 5)]

        }

        gsearch1=  GridSearchCV(estimator = XGBClassifier( learning_rate =0.1, n_estimators=20, max_depth=3,
            min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8,
            objective= 'binary:logistic', nthread=4, scale_pos_weight=1, seed=27),
            param_grid = param_test1, scoring='roc_auc',n_jobs=4, cv=5)


        gsearch1.fit(X_train, y_train)
        val_score=gsearch1.score(X_val, y_val)
        val_score_list.append(val_score)
        if val_score>val_score_best:
            val_score_best=val_score

            Optimal_parameters=gsearch1.best_params_ #optimal parameter




    return np.mean(val_score_list) ,Optimal_parameters


df=pd.read_csv('./data/2/train.csv')

kkp = [i for i in list(df)]
kkp.remove('label')
data_all=df.loc[:,kkp]


label_all=df.loc[:,['label']]

val_score_mean,parameters_best=Model_tmp(data_all,label_all)

print("average score of the 5-fold cross validation：",val_score_mean)
print("optimal parameter：",parameters_best)