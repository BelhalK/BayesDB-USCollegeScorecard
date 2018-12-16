import bayeslite
from bayeslite.read_pandas import bayesdb_read_pandas_df
import bdbcontrib
from bdbcontrib import cursor_to_df as df
from bdbcontrib.recipes import quickstart
import pandas as pd
import numpy
import re
import matplotlib
from matplotlib import ft2font
import matplotlib.pyplot as plt

from bdbcontrib.recipes import quickstart
import crosscat
import crosscat.MultiprocessingEngine as ccme
import bayeslite.metamodels.crosscat
import os
DATA = pd.read_csv("Most+Recent+Cohorts+(All+Data+Elements).csv", delimiter=',', low_memory = False)
df =DATA.loc[:,['OPEID','ADM_RATE_ALL',
                'SATVR25', 'SATVRMID','SATVR75','SATMT25','SATMTMID', 
                'SATMT75', 'SATWR25',   'SATWRMID', 'SATWR75', 'SAT_AVG_ALL',
                'ACTCM25', 'ACTCMMID','ACTCM75', 
                'TUITIONFEE_PROG','year',
                'st_fips', 'region', 'locale2',
               'CCBASIC', 'CCUGPROF', 'HBCU','UGDS',
               'PBI', 'ANNHI', 'TRIBAL', 'AANAPII',
               'HSI','NANTI', 'MENONLY', 'WOMENONLY', 'RELAFFIL',
               'PCIP01','PCIP03','PCIP04','PCIP05','PCIP09','PCIP10'
               ,'PCIP11','PCIP12','PCIP13','PCIP14','PCIP15','PCIP16','PCIP19','PCIP22'
               ,'PCIP23','PCIP24','PCIP25','PCIP26','PCIP27','PCIP29','PCIP30'
               ,'PCIP31','PCIP38','PCIP39','PCIP40','PCIP41'
                ,'PCIP42','PCIP43','PCIP44','PCIP45','PCIP46','PCIP47','PCIP48'
               ,'PCIP49','PCIP50','PCIP51','PCIP52','PCIP54'
               ,'AVGFACSAL','PFTFAC', 'PCTPELL', 'C150_4', 'DEATH_YR2_RT', 'COMP_ORIG_YR2_RT'
               , 'LO_INC_DEATH_YR2_R', 'LO_INC_COMP_ORIG_Y'
               , 'MD_INC_DEATH_YR2_R', 'MD_INC_COMP_ORIG_Y'
               , 'HI_INC_DEATH_YR2_R', 'HI_INC_COMP_ORIG_Y'
               , 'PELL_DEATH_YR2_RT', 'PELL_COMP_ORIG_YR2'
               , 'NOPELL_DEATH_YR2_RT', 'NOPELL_COMP_ORIG_YR2'
               , 'LOAN_DEATH_YR2_RT', 'LOAN_COMP_ORIG_YR2'
               , 'NOLOAN_DEATH_YR2_RT', 'NOLOAN_COMP_ORIG_YR2'
               , 'NOLOAN_ENRL_ORIG_YR', 'COMPL_RPY_1YR_RT'
               , 'NONCOMPL_RPY_1YR_RT', 'LO_INC_RPY_1YR_RT'
               , 'MD_INC_RPY_1YR_RT', 'HI_INC_RPY_1YR_RT'
               , 'DEP_RPY_1YR_RT', 'IND_RPY_1YR_RT'
               , 'COMPL_RPY_3YR_RT'
               , 'NONCOMPL_RPY_3YR_RT','LO_INC_RPY_3YR_RT'
               , 'MD_INC_RPY_3YR_RT', 'HI_INC_RPY_3YR_RT'
               , 'DEP_RPY_3YR_RT', 'IND_RPY_3YR_RT'
               , 'COMPL_RPY_5YR_RT'
               , 'NONCOMPL_RPY_5YR_RT', 'LO_INC_RPY_5YR_RT'
               , 'MD_INC_RPY_5YR_RT', 'HI_INC_RPY_5YR_RT'
               , 'DEP_RPY_5YR_RT', 'IND_RPY_5YR_RT'
               ,'DEBT_MDN', 'GRAD_DEBT_MDN'
               ,'WDRAW_DEBT_MDN', 'LO_INC_DEBT_MDN'
               ,'MD_INC_DEBT_MDN', 'HI_INC_DEBT_MDN'
               ,'DEP_DEBT_MDN', 'IND_DEBT_MDN'
               ,'faminc', 'md_faminc'
               ,'mn_earn_wne_p10', 'md_earn_wne_p10'
               ,'pct10_earn_wne_p10', 'pct25_earn_wne_p10'
               ,'pct75_earn_wne_p10', 'pct90_earn_wne_p10']] 

bdb = bayeslite.bayesdb_open("df.bdb")
bdbcontrib.query(bdb,'drop generator df_cc')
bdbcontrib.query(bdb,'drop table df')
bayesdb_read_pandas_df(bdb, "df", df, create=True)
ed = quickstart(name='df', bdb_path='df.bdb')
q = ed.q

ed.analyze(models=32, minutes=1)