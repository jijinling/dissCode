from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve,auc
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False




# compute the confusion matrix
def compute_confusion_matrix(precited,expected):
    part = precited ^ expected             # classify the result, make the correct prediction to be 0 and the false prediction to be 1

    pcount=[0,0]
    for tmp_i in list(part):
        if tmp_i==0:
            pcount[0]=pcount[0]+1
        if tmp_i==1:
            pcount[1]=pcount[1]+1

# statistics of the calssification，pcount[0]: number of 0，pcount[1]: number of 1
    tp_list = list(precited & expected)    # convert the TP to list
    fp_list = list(precited & ~expected)   # convert the FP to list
    tp = tp_list.count(1)                  # compute the number of TP
    fp = fp_list.count(1)                  # compute the number of FP
    tn = pcount[0] - tp                    # compute the number of TN
    fn = pcount[1] - fp                    # compute the number of FN
    return tp, fp, tn, fn

df_train=pd.read_csv('./data/2/train.csv')
kkp = [i for i in list(df_train)]
kkp.remove('label')
data_train_all=df_train.loc[:,kkp]
label_train_all=df_train.loc[:,['label']]


df_test=pd.read_csv('./data/2/test.csv')
kkp1 = [i for i in list(df_test)]
kkp1.remove('label')
data_test_all=df_test.loc[:,kkp1]
label_test_all=df_test.loc[:,['label']]



RF_model =  RandomForestClassifier()
RF_model.fit(data_train_all, label_train_all)
print("before optimizaiton of HP_score of training set：",round((RF_model.score(data_train_all, label_train_all)),3))
print("before optimization of Hp_score of test set：",round((RF_model.score(data_test_all, label_test_all)),3))


predSvmc_train_label = RF_model.predict(data_train_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_train_all['label'].tolist()),predSvmc_train_label)
Sensitivity_train = tp/(tp+fn)
Specificity_train = tn/(tn+fp)
Geometric_Accuracy_train=pow((Sensitivity_train*Specificity_train),0.5)
print('Sensitivity_train：',Sensitivity_train)
print('Specificity_train：',Specificity_train)
print('Geometric_Accuracy_train：',Geometric_Accuracy_train)

predSvmc_test_label = RF_model.predict(data_test_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_test_all['label'].tolist()),predSvmc_test_label)
Sensitivity_test = tp/(tp+fn)
Specificity_test = tn/(tn+fp)
Geometric_Accuracy_test=pow((Sensitivity_test*Specificity_test),0.5)
print('Sensitivity_test：',Sensitivity_test)
print('Specificity_test：',Specificity_test)
print('Geometric_Accuracy_test：',Geometric_Accuracy_test)



predRF_train = RF_model.predict_proba(data_train_all)
predRF_train=[i1[1] for i1 in predRF_train]
fpr_train, tpr_train, _ = roc_curve(label_train_all,predRF_train)
roc_auc_train = auc(fpr_train, tpr_train)
plt.plot(fpr_train, tpr_train,'b-', alpha=0.5, linewidth=2, label=str('training set：(AUC=%0.2f)' % (roc_auc_train)))



predRF_test = RF_model.predict_proba(data_test_all)
predRF_test=[i1[1] for i1 in predRF_test]
fpr_test, tpr_test, _ = roc_curve(label_test_all,predRF_test)
roc_auc_test = auc(fpr_test, tpr_test)
plt.plot(fpr_test, tpr_test,'r-', alpha=0.5, linewidth=2, label=str('test set：(AUC=%0.2f)' % (roc_auc_test)))

plt.title('RF model of the default parameter')
plt.legend(bbox_to_anchor=(0.63, 0.027), loc=3,borderaxespad=0)
plt.savefig('./output/RF/2/before_optimization_.png', dpi=600)



plt.clf()  #clear
print(               )
print('#####################################################')


#1: {'n_estimators': 700, 'min_samples_split': 2, 'min_samples_leaf': 1, 'max_features': 'sqrt', 'max_depth': 280}
#2:{'n_estimators': 1100, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 'auto', 'max_depth': 80}

RF_model = RandomForestClassifier(n_estimators=1100, min_samples_split=2,max_features='auto',max_depth=80)
RF_model.fit(data_train_all, label_train_all)
print("after optimization of HP_score of training set：",round((RF_model.score(data_train_all, label_train_all)),3))
print("after optimization of HP_score of test set：",round((RF_model.score(data_test_all, label_test_all)),3))

predSvmc_train_label = RF_model.predict(data_train_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_train_all['label'].tolist()),predSvmc_train_label)
Sensitivity_train = tp/(tp+fn)
Specificity_train = tn/(tn+fp)
Geometric_Accuracy_train=pow((Sensitivity_train*Specificity_train),0.5)
print('Sensitivity_train：',Sensitivity_train)
print('Specificity_train：',Specificity_train)
print('Geometric_Accuracy_train：',Geometric_Accuracy_train)

predSvmc_test_label = RF_model.predict(data_test_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_test_all['label'].tolist()),predSvmc_test_label)
Sensitivity_test = tp/(tp+fn)
Specificity_test = tn/(tn+fp)
Geometric_Accuracy_test=pow((Sensitivity_test*Specificity_test),0.5)
print('Sensitivity_test：',Sensitivity_test)
print('Specificity_test：',Specificity_test)
print('Geometric_Accuracy_test：',Geometric_Accuracy_test)






predRF_train = RF_model.predict_proba(data_train_all)
predRF_train=[i1[1] for i1 in predRF_train]
fpr_train, tpr_train, _ = roc_curve(label_train_all,predRF_train)
roc_auc_train = auc(fpr_train, tpr_train)
plt.plot(fpr_train, tpr_train,'b-', alpha=0.5, linewidth=2, label=str('training set：(AUC=%0.2f)' % (roc_auc_train)))



predRF_test = RF_model.predict_proba(data_test_all)
predRF_test=[i1[1] for i1 in predRF_test]
fpr_test, tpr_test, _ = roc_curve(label_test_all,predRF_test)
roc_auc_test = auc(fpr_test, tpr_test)
plt.plot(fpr_test, tpr_test,'r-', alpha=0.5, linewidth=2, label=str('test set：(AUC=%0.2f)' % (roc_auc_test)))

plt.title('RF model of the optimal parameter')
plt.legend(bbox_to_anchor=(0.63, 0.027), loc=3,borderaxespad=0)
plt.savefig('./output/RF/2/after_optimization_.png', dpi=600)




