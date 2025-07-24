# ############# openxlab ############
# import openxlab
# openxlab.login(ak='dbamykpr0g8wmjq5goe1', sk='lbk8yzqp6jlo21vmor0vw8lyqo4gmz53xx9nrqng') # 进行登录，输入对应的AK/SK，可在个人中心查看AK/SK
#
# from openxlab.dataset import info
#
# info(dataset_repo='OpenDataLab/ETT')  # 数据集信息及文件列表查看
#
# from openxlab.dataset import get
#
# get(dataset_repo='OpenDataLab/ETT', target_path='D:\Tool\PycharmTest\experimentalCode\experiment\Data')  # 数据集下载
#
# from openxlab.dataset import download
#
# download(dataset_repo='OpenDataLab/ETT', source_path='/README.md', target_path='D:\Tool\PycharmTest\experimentalCode\experiment\Data')  # 数据集文件下载

import pandas as pd

# === 1. 加载 Auto MPG 原始数据 ===
url_mpg = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
col_names_mpg = [
    "mpg","cylinders","displacement","horsepower",
    "weight","acceleration","model_year","origin","car_name"
]
df_mpg = pd.read_csv(
    url_mpg,
    delim_whitespace=True,
    names=col_names_mpg,
    na_values="?"
)
# 保存为本地 CSV
df_mpg.to_csv("auto_mpg_raw.csv", index=False)
print("Auto MPG 预览：")
print(df_mpg.head(), "\n")

# === 2. 加载 Diabetes 原始数据 ===
url_diabetes = "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt"
df_diabetes = pd.read_csv(
    url_diabetes,
    sep="\t"
)
# 保存为本地 CSV
df_diabetes.to_csv("diabetes_raw.csv", index=False)
print("Diabetes 数据预览：")
print(df_diabetes.head())
