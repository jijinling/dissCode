from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False





def compute_confusion_matrix(precited,expected):
    part = precited ^ expected
    pcount=[0,0]
    for tmp_i in list(part):
        if tmp_i==0:
            pcount[0]=pcount[0]+1
        if tmp_i==1:
            pcount[1]=pcount[1]+1

    tp_list = list(precited & expected)
    fp_list = list(precited & ~expected)
    tp = tp_list.count(1)
    fp = fp_list.count(1)
    tn = pcount[0] - tp
    fn = pcount[1] - fp
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


SVC_model = svm.SVC(probability=True)
SVC_model.fit(data_train_all, label_train_all)
print("before optimizaiton of HP_score of training set：",round((SVC_model.score(data_train_all, label_train_all)),3))
print("before optimizaiton of HP_score of test set：",round((SVC_model.score(data_test_all, label_test_all)),3))


predSvmc_train_label = SVC_model.predict(data_train_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_train_all['label'].tolist()),predSvmc_train_label)
Sensitivity_train = tp/(tp+fn)
Specificity_train = tn/(tn+fp)
Geometric_Accuracy_train=pow((Sensitivity_train*Specificity_train),0.5)
print('Sensitivity_train：',Sensitivity_train)
print('Specificity_train：',Specificity_train)
print('Geometric_Accuracy_train：',Geometric_Accuracy_train)


predSvmc_test_label = SVC_model.predict(data_test_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_test_all['label'].tolist()),predSvmc_test_label)
Sensitivity_test = tp/(tp+fn)
Specificity_test = tn/(tn+fp)
Geometric_Accuracy_test=pow((Sensitivity_test*Specificity_test),0.5)
print('Sensitivity_test：',Sensitivity_test)
print('Specificity_test：',Specificity_test)
print('Geometric_Accuracy_test：',Geometric_Accuracy_test)



predSvmc_train = SVC_model.predict_proba(data_train_all)
predSvmc_train=[i1[1] for i1 in predSvmc_train]
fpr_train, tpr_train, _ = roc_curve(label_train_all,predSvmc_train)
roc_auc_train = auc(fpr_train, tpr_train)
plt.plot(fpr_train, tpr_train,'b-', alpha=0.5, linewidth=2, label=str('training set：(AUC=%0.2f)' % (roc_auc_train)))




predSvmc_test = SVC_model.predict_proba(data_test_all)
predSvmc_test=[i1[1] for i1 in predSvmc_test]
fpr_test, tpr_test, _ = roc_curve(label_test_all,predSvmc_test)
roc_auc_test = auc(fpr_test, tpr_test)
plt.plot(fpr_test, tpr_test,'r-', alpha=0.5, linewidth=2, label=str('test set：(AUC=%0.2f)' % (roc_auc_test)))

plt.title('SVM model of default parameter')
plt.legend(bbox_to_anchor=(0.63, 0.027), loc=3,borderaxespad=0)
plt.savefig('./output/SVC/2/before_optimization_.png', dpi=600)



plt.clf()
print(               )
print('#####################################################')

# 2 最优参数： {'svc__C': 10.0, 'svc__gamma': 0.0001, 'svc__kernel': 'rbf'} #cannot adjust gamma, this parameter is identified by String
# 1 最优参数： {'svc__C': 0.01, 'svc__kernel': 'linear'}
SVC_model = svm.SVC(kernel='rbf',C=10.0, probability=True)
SVC_model.fit(data_train_all, label_train_all)
print("after optimizaiton of HP_score of training set：",round((SVC_model.score(data_train_all, label_train_all)),3))
print("after optimizaiton of HP_score of test set：",round((SVC_model.score(data_test_all, label_test_all)),3))



predSvmc_train_label = SVC_model.predict(data_train_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_train_all['label'].tolist()),predSvmc_train_label)
Sensitivity_train = tp/(tp+fn)
Specificity_train = tn/(tn+fp)
Geometric_Accuracy_train=pow((Sensitivity_train*Specificity_train),0.5)
print('Sensitivity_train：',Sensitivity_train)
print('Specificity_train：',Specificity_train)
print('Geometric_Accuracy_train：',Geometric_Accuracy_train)


predSvmc_test_label = SVC_model.predict(data_test_all)
tp, fp, tn, fn = compute_confusion_matrix(np.array(label_test_all['label'].tolist()),predSvmc_test_label)
Sensitivity_test = tp/(tp+fn)
Specificity_test = tn/(tn+fp)
Geometric_Accuracy_test=pow((Sensitivity_test*Specificity_test),0.5)
print('Sensitivity_test：',Sensitivity_test)
print('Specificity_test：',Specificity_test)
print('Geometric_Accuracy_test：',Geometric_Accuracy_test)



predSvmc_train = SVC_model.predict_proba(data_train_all)
predSvmc_train=[i1[1] for i1 in predSvmc_train]
fpr_train, tpr_train, _ = roc_curve(label_train_all,predSvmc_train)
roc_auc_train = auc(fpr_train, tpr_train)
plt.plot(fpr_train, tpr_train,'b-', alpha=0.5, linewidth=2, label=str('training set：(AUC=%0.2f)' % (roc_auc_train)))



predSvmc_test = SVC_model.predict_proba(data_test_all)
predSvmc_test=[i1[1] for i1 in predSvmc_test]
fpr_test, tpr_test, _ = roc_curve(label_test_all,predSvmc_test)
roc_auc_test = auc(fpr_test, tpr_test)
plt.plot(fpr_test, tpr_test,'r-', alpha=0.5, linewidth=2, label=str('test set：(AUC=%0.2f)' % (roc_auc_test)))

plt.title('SVM model of optimal parameter')
plt.legend(bbox_to_anchor=(0.63, 0.027), loc=3,borderaxespad=0)  # 显示上面的label #很重要，不可删除 bbox_to_anchor 是调整label位置
plt.savefig('./output/SVC/2/after optimization.png', dpi=600)


