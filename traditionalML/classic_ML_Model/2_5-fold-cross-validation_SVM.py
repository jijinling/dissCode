import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC





def Model_tmp(data1,info1):
    val_score_list=[]
    folds = KFold(n_splits=5, shuffle=True, random_state=1)
    val_score_best=0
    for train_index, test_index in folds.split(data1):  # call the split() to split data
        X_train  = data1.iloc[train_index,:]
        X_val = data1.iloc[test_index,:]

        train_label = info1.iloc[train_index,:]
        val_label = info1.iloc[test_index, :]


        y_train = train_label.values.ravel()
        y_val = val_label.values.ravel()


        param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
        param_grid = [{'svc__C': param_range,
                       'svc__kernel': ['linear']},
                      {'svc__C': param_range,
                       'svc__kernel': ['rbf'],
                       'svc__gamma': param_range}]

        pipe_svc = make_pipeline(StandardScaler(), SVC(random_state=1))

        gs = GridSearchCV(estimator=pipe_svc,
                          param_grid=param_grid,
                          scoring='accuracy',
                          cv=10,
                          n_jobs=-1)
        gs = gs.fit(X_train, y_train)
        clf = gs.best_estimator_
        clf.fit(X_train, y_train)

        val_score=clf.score(X_val, y_val)
        val_score_list.append(val_score)
        if val_score>val_score_best:
            val_score_best=val_score
            Optimal_parameters=gs.best_params_ #optimal parameter

    return np.mean(val_score_list) ,Optimal_parameters


df=pd.read_csv('./data/2/train.csv')

kkp = [i for i in list(df)]
kkp.remove('label')
data_all=df.loc[:,kkp]


label_all=df.loc[:,['label']]

val_score_mean,parameters_best=Model_tmp(data_all,label_all)

print("average score of the 5-fold cross validation：",val_score_mean)
print("optimal parameter：",parameters_best)