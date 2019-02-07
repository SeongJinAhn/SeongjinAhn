import pandas as pd
import numpy as np

KOSPI = pd.read_excel('./titanic/input/kospi.xlsx')
column=[]
for x in KOSPI.columns:
    column.append(''.join(x.split('\n')))
KOSPI.columns = column
PBR = pd.read_excel('./titanic/input/kospi_PBR_20171101.xlsx')
PBR['총카운트'] = PBR['종목명'].apply(lambda x : KOSPI_long[x]['2017/06/01'] if x in KOSPI.columns else np.NaN)
PBR_long = pd.melt(PBR,id_vars = ['일자','종목코드','종목명'],var_name='var_name')
PBR_long = PBR.set_index('종목명')
