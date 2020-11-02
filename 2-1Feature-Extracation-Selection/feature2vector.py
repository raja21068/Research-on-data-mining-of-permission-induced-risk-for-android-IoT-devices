# -*- coding: utf-8 -*-

import pandas as pd
import codecs
import os

FEATURE_PATH = "../data/features.txt"
BASE_PATH = "../data/static/malicious/virusTotal/"


def get_feature_dict():
    """
   
    :return:
    """
    with codecs.open(FEATURE_PATH, "r") as f:
        feature_list = f.read().split("\n")
    feature_dict = {}
    for v in feature_list:
        feature_dict[v] = 0
    return feature_dict


def preprocessing(x):
    """
    
    :param x:
    :return:
    """
    # 格式处理
    t = x.split("intent.")
    if len(t) > 1:
        return t[1]
    else:
        return x


def get_feature(path):
    """
   
    :param path:
    :return:
    """
    with codecs.open(path, "r") as f:
        feature_list = f.read().split("\n")
    feature_list = list(set(feature_list))
    return list(map(preprocessing, feature_list))


apks = os.listdir(BASE_PATH)
vecs = []
for apk in apks:
    feature_dict = get_feature_dict()
    real_path = os.path.join(BASE_PATH, apk)
    feature = get_feature(real_path)
    for f in feature:
        if f in feature_dict.keys():
            feature_dict[f] = 1
    feature_dict["sample"] = apk.split(".")[0]
    vec = []
    columns = []
    for key, value in feature_dict.items():
        vec.append(value)
        columns.append(key)
    vecs.append(vec)
df = pd.DataFrame(vecs, columns=columns)
df.to_csv("virusTotal - 1500.csv", index=False)
