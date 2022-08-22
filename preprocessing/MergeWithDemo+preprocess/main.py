import os
import xml.dom.minidom as xmldom
import pandas as pd
import csv

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#map the relationship from study uid to subject id
from choose_from_ADNIMERGE import choose_from_ADNIMERGE
from choose_from_PTDEMOG import choose_from_PTDEMOG


def extract_IDinfo(file_dir):
    dict = {}
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            dom_obj=xmldom.parse(os.path.join(root,file))
            element_obj=dom_obj.documentElement
            tag1=element_obj.getElementsByTagName("study")
            for i in range(len(tag1)):
                study_uid = tag1[i].getAttribute("uid")
            tag2=element_obj.getElementsByTagName("subject")
            for i in range(len(tag2)):
                subject_id=tag2[i].getAttribute("id")
            dict[study_uid]=subject_id
    return dict

# map the relationship from rid to study uid and also subject id
def find_ids():
    allMap={}

    dict_AD=extract_IDinfo('data/AD_meta')
    dict_CN=extract_IDinfo('data/CN_meta')
    with open("data/id-suid-map.csv", "r") as csvfile:
        reader = pd.read_csv("data/id-suid-map.csv")
        lines = reader.values.tolist()
        for line in lines:
            studyID = str(line[1])
            if studyID in dict_AD.keys():
                rid = str(line[2])
                allMap[rid]=[studyID,dict_AD[studyID]]  #{rid:[studyID, subjectID]}
            if studyID in dict_CN.keys():
                rid = str(line[2])
                allMap[rid]=[studyID,dict_CN[studyID]]  #{rid:[studyID, subjectID]}
    return allMap

# create the chosen demographic data (only 100 subjects): like age, marry, education, race, work......
def create_demographicdata():
    allMap = find_ids()

    choose_from_ADNIMERGE()
    choose_from_PTDEMOG()

    # first merge the two csv file into one, using the common field RID
    with open('data/chosen_ADNIMERGE.csv', "r"):
        reader1 = pd.read_csv('data/chosen_ADNIMERGE.csv')

    with open('data/chosen_PTDEMOG.csv', "r"):
        reader2 = pd.read_csv('data/chosen_PTDEMOG.csv')

    mergefile = pd.merge(reader1, reader2, how='inner', on=['RID', 'RID'])
    mergefile.to_csv('data/all_demodata.csv', sep=',', index=False)

    # then,filter to find the only 100 subjects
    with open("data/all_demodata.csv", "r") as fAll:
        readerAll = pd.read_csv("data/all_demodata.csv")
        readerall2 = csv.DictReader(fAll)
        headers = readerall2.fieldnames
        headers.insert(0, 'subjectID')
        lines = readerAll.values.tolist()

    with open("data/demographic100.csv", 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        subject_ids = set()
        for line in lines:
            rid = str(line[0])
            if rid in allMap.keys():
                row = line
                row.insert(0, allMap[rid][1])
                if line[0] not in subject_ids:
                    writer.writerow(row)
                    subject_ids.add(line[0])

# delete the unrelated column of demographic100
def delete_unrelated_column():
    with open('data/demographic100.csv', "r"):
        reader1 = pd.read_csv('data/demographic100.csv')
        reader1 = reader1.drop(['RID', 'ID'], axis=1)
        reader1.to_csv('data/demographic100.csv', index=False)



def merge_demographic_with_volumnData():
    create_demographicdata()
    delete_unrelated_column()

    with open('data/demographic100.csv', "r"):
        reader1 = pd.read_csv('data/demographic100.csv')

    with open('data/subcorticalData.csv', "r"):
        reader2 = pd.read_csv('data/subcorticalData.csv')

    mergefile = pd.merge(reader1, reader2, how='inner', on=['subjectID', 'subjectID'])
    mergefile.to_csv('outputdata/demographic_with_volumn.csv', index=False)


def post_process_colVal():
    merge_demographic_with_volumnData()
    with open("outputdata/demographic_with_volumn.csv", "r") as f1:
        reader1 = pd.read_csv("outputdata/demographic_with_volumn.csv")
        lines = reader1.values.tolist()
        reader2 = csv.DictReader(f1)
        headers = reader2.fieldnames


    with open("outputdata/demographic_with_volumn.csv", 'w', newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(headers)

        for line in lines:
            ethnicity = line[2]
            race = line[3]
            education = line[7]

            if ethnicity == "Not Hisp/Latino":
                ethnicity = 0
            else:
                ethnicity = 1
            if race == "White":
                race = 0
            else:
                race = 1
            if education < 1.0:
                education = 0
            elif 1.0<=education<=2.0:
                education = 1.0
            elif 2.0<education<=7.0:
                education = 2
            elif 7.0<education<=15.0:
                education = 3
            else:
                education = 4

            line[2] = ethnicity
            line[3] = race
            line[7] = education

            writer.writerow(line)



def add_aparc():
    post_process_colVal()
    with open('outputdata/demographic_with_volumn.csv', "r"):
        reader1 = pd.read_csv('outputdata/demographic_with_volumn.csv')

    with open('data/RegionArea.csv', "r"):
        reader2 = pd.read_csv('data/RegionArea.csv')

    mergefile = pd.merge(reader1, reader2, how='inner', on=['subjectID', 'subjectID'])
    mergefile.to_csv('outputdata/demographic_with_volumn_with_area.csv', index=False)


def remove_subjectID():
    add_aparc()
    with open('outputdata/demographic_with_volumn_with_area.csv', "r"):
        reader1 = pd.read_csv('outputdata/demographic_with_volumn_with_area.csv')
        reader1 = reader1.drop(['subjectID'], axis=1)
        reader1.to_csv('outputdata/demographic_with_volumn_with_area.csv', index=False)

    with open('outputdata/demographic_with_volumn.csv', "r"):
        reader1 = pd.read_csv('outputdata/demographic_with_volumn.csv')
        reader1 = reader1.drop(['subjectID'], axis=1)
        reader1.to_csv('outputdata/demographic_with_volumn.csv', index=False)








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    remove_subjectID()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
