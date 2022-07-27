# -*- coding:utf-8 -*-

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import random


def xml_to_csv(path):
    xml_list = []
    xml_list_test = []
    # 设置训练集所占比例
    rate = 1
    i = 0
    img_file = glob.glob(path + '/*.xml')
    random.shuffle(img_file)
    for xml_file in img_file:
        i = i + 1
        num_of_train = int(len(glob.glob(path + '/*.xml')) * rate)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        if i <= num_of_train:
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
            # print(xml_list)
        else:
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list_test.append(value)
            # print(xml_list_test)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df_test = pd.DataFrame(xml_list_test, columns=column_name)
    return xml_df, xml_df_test


def main():
    # xml文件的存储地址，根据自己xml存储路径进行调整
    image_path = os.path.join('D:/PyCharm/DataSet/data-952/Annotations/')
    # csv文件保存位置，自行调/
    # 训练集
    csv_save_path = 'D:/PyCharm/DataSet/data-952/csv/train.csv'
    # 测试集
    # csv_save_path_test = 'D:/PyCharm/DataSet/data-952/csv/test.csv'

    xml_df, xml_df_test = xml_to_csv(image_path)
    xml_df.to_csv(csv_save_path, index=None)
    # xml_df_test.to_csv(csv_save_path_test, index=None)
    print('Successfully converted xml to csv.')


main()
