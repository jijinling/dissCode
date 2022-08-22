import numpy as np
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV



def Model_tmp(data1,info1):
    val_score_list=[]
    folds = KFold(n_splits=5, shuffle=True, random_state=1)
    val_score_best=0
    for train_index, test_index in folds.split(data1):  # call the split method to split data
        X_train  = data1.iloc[train_index,:]
        X_val = data1.iloc[test_index,:]

        train_label = info1.iloc[train_index,:]
        val_label = info1.iloc[test_index, :]


        y_train = train_label.values.ravel()
        y_val = val_label.values.ravel()

        n_estimators_range = [int(x) for x in np.linspace(start=50, stop=3000, num=60)]
        max_features_range = ['auto', 'sqrt']
        max_depth_range = [int(x) for x in np.linspace(10, 500, num=50)]
        max_depth_range.append(None)
        min_samples_split_range = [2, 5, 10]
        min_samples_leaf_range = [1, 2, 4, 8]

        random_forest_hp_range = {'n_estimators': n_estimators_range,
                                  'max_features': max_features_range,
                                  'max_depth': max_depth_range,
                                  'min_samples_split': min_samples_split_range,
                                  'min_samples_leaf': min_samples_leaf_range
                                  }

        random_forest_model_test_base = RandomForestClassifier()
        random_forest_model_test_random = RandomizedSearchCV(estimator=random_forest_model_test_base,
                                                             param_distributions=random_forest_hp_range,
                                                             n_iter=10,
                                                             n_jobs=-1,
                                                             cv=5,
                                                             verbose=1
                                                             )
        random_forest_model_test_random.fit(X_train, y_train)

        val_score=random_forest_model_test_random.score(X_val, y_val)
        val_score_list.append(val_score)

        if val_score>val_score_best:
            val_score_best=val_score
            Optimal_parameters=random_forest_model_test_random.best_params_ #optimal hyper parameter
    return np.mean(val_score_list) ,Optimal_parameters


df=pd.read_csv('./data/2/train.csv')

kkp = [i for i in list(df)]
kkp.remove('label')
data_all=df.loc[:,kkp]


label_all=df.loc[:,['label']]

val_score_mean,parameters_best=Model_tmp(data_all,label_all)

print("average score of the 5-fold cross validation：",val_score_mean)
print("optimal parameter：",parameters_best)