# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:46:10 2019

@author: Kratik Saxena
"""

from mailmerge import MailMerge
from datetime import date

#df=pd.read_csv('PythonExport.csv')
#print(df.iloc[0,1])

template = "TEMPLATE.docx"
document = MailMerge(template)
print(document.get_merge_fields())
di={"Name":"Sherni"}
document.merge(
    X_PAT_1_NUMBER ='Gold',
    X_PAT_2_NUMBER ='Springfield',
    X_PAT_3_NUMBER = 'US',
    X_PAT_1_TITLE = 'abc',
    X_PAT_2_TITLE = 'bca',
    X_PAT_3_TITLE = 'cab',
    X_PAT_1_ASSIGNEE = 'xyz',
    X_PAT_2_ASSIGNEE = 'yzx',
    X_PAT_3_ASSIGNEE = 'zxy',
    X_PAT_1_PUBDATE = 'qwe',
    X_PAT_2_PUBDATE = 'weq',
    X_PAT_3_PUBDATE = 'eqw',
    X_PAT_1_APPDATE = 'alsmj',
    X_PAT_2_APPDATE = 'alsmj',
    X_PAT_3_APPDATE = 'alsmj',
    X_PAT_1_PRIORDATE = 'lksd',
    X_PAT_2_PRIORDATE = 'lksd',
    X_PAT_3_PRIORDATE = 'lksd',
    Y_PAT_1_NUMBER = 'JBSHWGD',
	Y_PAT_1_TITLE = 'ASAD',
    Y_PAT_1_ASSIGNEE = "ASAD",
    Y_PAT_1_PUBDATE = "ASAD",
    Y_PAT_1_APPDATE = "ASAD",
    Y_PAT_1_PRIORDATE = "ASAD",
    Y_PAT_2_NUMBER = "ASAD",
	Y_PAT_2_TITLE = "ASAD",
    Y_PAT_2_ASSIGNEE = "ASAD",
    Y_PAT_2_PUBDATE = "ASAD",
    Y_PAT_2_APPDATE = "ASAD",
    Y_PAT_2_PRIORDATE = "ASAD",
    Y_PAT_3_NUMBER = "ASAD",
    Y_PAT_3_TITLE = "ASAD",
    Y_PAT_3_ASSIGNEE = "ASAD",
    Y_PAT_3_PUBDATE = "ASAD",
    Y_PAT_3_APPDATE = "ASAD",
    Y_PAT_3_PRIORDATE = "ASAD",
    X_PAT_1_FAMILY = 'ABC, ABCV,CBYGD',
    X_PAT_1_INVETORS = 'KRATIK, saxena')

document.write('NEW REPORT.docx')
# plan  to dump data in a file