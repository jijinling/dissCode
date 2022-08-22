import pandas as pd


input_path1=r'./data/1/demographic_with_volumn.csv'
output_path1=r'./data/1/demographic_with_volumn_new.csv'


input_path2=r'./data/2/demographic_with_volumn_with_area.csv'
output_path2=r'./data/2/demographic_with_volumn_with_area_new.csv'


#feature selection; delete the same column, delete the non-numeric column( only one column: work), compute the MAD, select the highly correlation column
def preprocess(input_path,output_path,corr_float):
    df=pd.read_csv(input_path)
    new_df1 = df.loc[:, (df != df.iloc[0]).any()]  #delete all the same feature column
    ######################apart the non-numeric column from the numeric column
    size  =  new_df1.shape
    judge = ["int64", "float64"]
    values = new_df1.columns.values
    new_df2 = pd.DataFrame()
    for i1 in range(size[1]):
        if df.iloc[:, i1].dtype in judge:
            new_df2[values[i1]] = df.iloc[:, i1]


    ############compute the middle value and the absolute deviation#########
    tez=new_df2.mad().index.tolist()
    z=new_df2.mad().tolist()
    k_list=[]
    for i2 in range(len(z)):
        if z[i2] > 0.01 :
            k_list.append(tez[i2])
    new_df3=new_df2.loc[:,k_list]

    k_list_value=[]
    for i3 in k_list:
        list_R = new_df3[i3].tolist()
        k_list_value.append(list_R)

    # compute the correlation coefficient between each two columns
    data_dict = {}  # create the data dictionary to preparing for the dataframe
    for col, gf_lst in zip(k_list , k_list_value):
        data_dict[col] = gf_lst
    unstrtf_df = pd.DataFrame(data_dict)
    cor1 = unstrtf_df.corr()  # compute the correlation coefficient, and get a matrix
    correlated_features = set()
    correlation_matrix =cor1
    for i4 in range(len(correlation_matrix.columns)):
        for j in range(i4):
            if abs(correlation_matrix.iloc[i4,j])>corr_float:
                colname=correlation_matrix.columns[i4]
                correlated_features.add(colname)

    new_df3.drop(labels=correlated_features, axis=1, inplace=True)

    kkp=[i for i in list(new_df3)]
    try:

        kkp.remove('Unnamed: 0')
    except:
        pass
    pppp=df.loc[:,['label']+kkp]

    pppp=pppp.dropna(axis='columns', how='any')

    pppp.to_csv(output_path, index=False, encoding='utf-8-sig')




preprocess(input_path1,output_path1,corr_float=0.8)

preprocess(input_path2,output_path2,corr_float=0.8)

