import pandas as pd
import numpy as np
import dask.dataframe as dd


import pickle

import random


random.seed(42)
list = range(0,1051430459)
sample_list = random.sample(list, 150000)

with open("/home/shkim/testfolder/abnoral-detection-lanl2015/abnoral-detection-lanl2015/line_offset.pickle", "rb") as fr:
    line_offset = pickle.load(fr)

auth_cols = ["time", "suser_do", "duser_do", "scom", "dcom", "a_t", "logon_type", "a_ot", "s/f"]
df_auth_cols = ["time", "s_user", "s_domain",  "d_user","d_domain", "scom", "dcom", "a_t", "logon_type", "a_ot", "s/f"]
df_auth = pd.DataFrame(columns = df_auth_cols)
with open("/home/shkim/lanl2015/auth.txt", "r") as f:
    for cnt, i in enumerate(sample_list):
        f.seek(line_offset[i])
        line = f.readline()
        f.seek(0)
        # 진행상황 확인
        print(cnt + 1, "회 진행중")
        #  del null row
        

        # split    
        temp = pd.DataFrame([line.split(",")],columns = auth_cols)
        temp["s_user"] = temp.suser_do.str.split("@").str[0]
        temp["s_domain"] = temp.suser_do.str.split("@").str[1]
        temp["d_user"] = temp.duser_do.str.split("@").str[0]
        temp["d_domain"] = temp.duser_do.str.split("@").str[1]

        # '$' 삭제
        temp["s_user"][temp["s_user"].str[-1] == "$"] = temp["s_user"][temp["s_user"].str[-1] == "$"].str[:-1]
    
        # concat
        df_auth = pd.concat([df_auth, temp], join = "inner", axis = 0)


df_auth.to_csv("auth_sample.csv")