import numpy as np
import pandas as pd
from pandas import DataFrame

Trigonometric_table_path = r"table1.xlsx"
Trigonometric_table = pd.read_excel(Trigonometric_table_path)
Trigonometric_table.drop(Trigonometric_table.columns[[0,2,3]],axis=1,inplace=True)
Trigonometric_table.drop(Trigonometric_table.index[[0,1]],inplace=True)
data = {"col1": np.random.randint(10000000, 100000000, size=10000),
        "col2": np.random.randint(10000000, 100000000, size=10000),
        "real": "",
        "use_method": "",
        "error_rate": ""}
test_case: DataFrame = pd.DataFrame(data)
def find_near_cos_sin(sin_cos_0, goal):
    list_ = []
    list_1 = []
    list_2 = []

    for y in range(2,640):
        list_.append(abs(Trigonometric_table.loc[y, sin_cos_0] - goal))
        list_1.append(Trigonometric_table.loc[y, sin_cos_0])
        list_2.append(Trigonometric_table.loc[y, 'x'])
    return min(list_),list_2[list_.index(min(list_))],sin_cos_0
def find_near_degree(sin_cos_0,goal):
    list_ = []
    list_1 = []
    for w in range(2, 640):
        list_.append(abs(Trigonometric_table.loc[w, 'x'] - goal))
        list_1.append(Trigonometric_table.loc[w,sin_cos_0])
    return list_1[list_.index(min(list_))]
def panduan(data1, formula3):
    if data1 > 270:
        if formula3 == "sin(x)":
            return -find_near_degree("cos(x)",data1-270)
        elif formula3 == "cos":
            return find_near_degree("sin(x)",data1-270)
    elif data1 > 180:
        return -find_near_degree(formula3,data1-180)
    elif data1 > 90:
        if formula3 == "sin(x)":
            return find_near_degree("cos(x)",data1-90)
        elif formula3 == "cos(x)":
            return -find_near_degree("sin(x)",data1-90)
    elif data1 >= 0:
        return find_near_degree(formula3,data1)
    elif data1 < 0:
        return panduan(360 + data1, formula3)
def output(out0,out1,k):
    # test_case.loc[k, 'real'] = int(test_case.loc[k, "col1"]) * int(test_case.loc[k, "col2"])
    # test_case.loc[k, 'use_method'] = (out0 + out1) / 2*10000000000000000
    # test_case.loc[k, 'error_rate'] = abs(test_case.loc[k, 'real'] - test_case.loc[k, 'use_method']) / test_case.loc[k, 'real'] * 100
    # print(int(test_case.loc[k, "col1"]) * int(test_case.loc[k, "col2"]))
    print((out0 + out1) / 2*10000000000000000)
    # print(abs(test_case.loc[k, 'real'] - test_case.loc[k, 'use_method']) / test_case.loc[k, 'real'] * 100)

for k in range(1000):
    number0=test_case.loc[k,'col1']/100000000

    degree0_sin=find_near_cos_sin("sin(x)",number0)
    degree0_cos=find_near_cos_sin('cos(x)',number0)
    sin_cos_0=''
    degree0=0
    if degree0_sin[0]>degree0_cos[0]:
        sin_cos_0=degree0_cos[2]
        degree0=degree0_cos[1]
    else:
        sin_cos_0=degree0_sin[2]
        degree0=degree0_sin[1]



    ################################################
    number1=test_case.loc[k,'col2']/100000000

    degree1_sin=find_near_cos_sin("sin(x)",number0)
    degree1_cos=find_near_cos_sin('cos(x)',number0)
    sin_cos_1=''
    degree1=0
    if degree1_sin[0]>degree1_cos[0]:
        sin_cos_1=degree1_cos[2]
        degree1=degree1_cos[1]
    else:
        sin_cos_1=degree1_sin[2]
        degree1=degree1_sin[1]

##########################################################
    if sin_cos_0 == "sin(x)" and sin_cos_1 == "cos(x)":
        final1 = panduan(degree0 + degree1, sin_cos_0)
        final2 = panduan(degree0 - degree1, sin_cos_1)
        output(final1,final2,k)

    elif sin_cos_0 == "cos(x)" and sin_cos_1 == "sin(x)":
        final1 = panduan(degree1 + degree0, sin_cos_0)
        final2 = panduan(degree1 - degree0, sin_cos_1)

        output(final1,final2,k)
    elif sin_cos_0 == "cos(x)" and sin_cos_1 == "cos(x)":

        final1 = panduan(degree0 - degree1, sin_cos_0)

        final2 = panduan(degree0 + degree1, sin_cos_1)

        output(final1,final2,k)
    elif sin_cos_0 == "cos(x)" and sin_cos_1 == "sin(x)":

        final1 = panduan(degree0 - degree1, sin_cos_0)
        final2 = panduan(degree0 + degree1, sin_cos_1)

        output(final1,final2,k)
print(test_case)