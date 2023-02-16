import pandas as pd
import numpy as np
import dask.dataframe as dd


import pickle

import random


random.seed(42)
list = range(0,1051430459)
sample_list = random.sample(list, 50000)

with open("/home/shkim/testfolder/abnoral-detection-lanl2015/abnoral-detection-lanl2015/line_offset.pickle", "rb") as fr:
    line_offset = pickle.load(fr)


attack_log = pd.read_csv("/home/shkim/lanl2015/redteam.txt", names = ["time", "s_d", "scom", "dcom"]) # 공격 기록 저장

attack_log["s_user"] = attack_log.s_d.str.split("@").str[0]
attack_log["s_domain"] = attack_log.s_d.str.split("@").str[1]

attack_log.drop(["s_d"], axis = 1, inplace = True)

attack_log = attack_log[["time", "s_user","s_domain", "scom", "dcom"]]




attack_log.to_csv("attack_log.csv")