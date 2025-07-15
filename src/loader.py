import pandas as pd


#//////////////////////////////////Pandas를 활용해서 엑셀csv 읽어오기

DfLine1_upper = pd.read_csv("./data/Daegu1_upper.csv",encoding="ANSI")
DfLine1_lower = pd.read_csv("./data/Daegu1_lower.csv",encoding="ANSI")
DfLine2_upper = pd.read_csv("./data/Daegu2_upper.csv",encoding="ANSI")
DfLine2_lower = pd.read_csv("./data/Daegu2_lower.csv",encoding="ANSI")
DfLine3_upper = pd.read_csv("./data/Daegu3_upper.csv",encoding="ANSI")
DfLine3_lower = pd.read_csv("./data/Daegu3_lower.csv",encoding="ANSI")

#///////////////////////읽어온 데이터를 역 간 소요시간 데이터 만들기
DictInterval_data = {}


for i in range(DfLine1_upper.shape[0]-1):
    element = { DfLine1_upper["역명"].loc[i+1] : int(DfLine1_upper["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine1_upper["역명"].loc[i],{}).update(element)

for i in range(DfLine1_lower.shape[0]-1):
    element = { DfLine1_lower["역명"].loc[i+1] : int(DfLine1_lower["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine1_lower["역명"].loc[i],{}).update(element)

for i in range(DfLine2_upper.shape[0]-1):
    element = { DfLine2_upper["역명"].loc[i+1] : int(DfLine2_upper["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine2_upper["역명"].loc[i],{}).update(element)

for i in range(DfLine2_lower.shape[0]-1):
    element = { DfLine2_lower["역명"].loc[i+1] : int(DfLine2_lower["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine2_lower["역명"].loc[i],{}).update(element)

for i in range(DfLine3_upper.shape[0]-1):
    element = { DfLine3_upper["역명"].loc[i+1] : int(DfLine3_upper["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine3_upper["역명"].loc[i],{}).update(element)

for i in range(DfLine3_lower.shape[0]-1):
    element = { DfLine3_lower["역명"].loc[i+1] : int(DfLine3_lower["소요시간"].loc[i]) }
    DictInterval_data.setdefault(DfLine3_lower["역명"].loc[i],{}).update(element)


DfLines_upper = [DfLine1_upper,DfLine2_upper,DfLine3_upper]
DFLines_lower = [DfLine1_lower,DfLine2_lower,DfLine3_lower]