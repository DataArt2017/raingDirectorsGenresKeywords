# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:21:58 2017

@author: Farah Jasim
"""
from openpyxl import Workbook
import xlsxwriter
import xlrd
import json
import ast
import pandas as pd
from numpy import *
from pylab import *   
file_location = 'raingDirectorsGenresKeywords.xlsx';
file_location2 = 'snap2.xlsx';


wd = xlrd.open_workbook(file_location)
wr = xlsxwriter.Workbook(file_location2)

worksheet = wd.sheet_by_name('raingDirectorsGenresKeywords')
worksheet1 = wr.add_worksheet()



col0_id = 0
col5_keywords = 5

# tronsform the workbook to a list of dictionnary
data =[]
i = 0
row = 1
#read from the first row
str1 = worksheet.cell_value(row,col0_id)
str2 = worksheet.cell_value(row,col5_keywords)
st1 = worksheet.cell_value(row,1)
st2 = worksheet.cell_value(row,2)
st3 = worksheet.cell_value(row,3)
st4 = worksheet.cell_value(row,4)
st6 = worksheet.cell_value(row,6)
st7 = worksheet.cell_value(row,7)
st8 = worksheet.cell_value(row,8)
st9 = worksheet.cell_value(row,9)
st10 = worksheet.cell_value(row,10)
st11 = worksheet.cell_value(row,11)
st12 = worksheet.cell_value(row,12)
st13 = worksheet.cell_value(row,13)
st14 = worksheet.cell_value(row,14)
st15 = worksheet.cell_value(row,15)
st16 = worksheet.cell_value(row,16)
st17 = worksheet.cell_value(row,17)
st18 = worksheet.cell_value(row,18)
st19 = worksheet.cell_value(row,19)
st20 = worksheet.cell_value(row,20)

#worksheet1.write(row, 0,str1)
#worksheet1.write(row, 1,str2)
j = 1
rowsheet2 = 1
for row in range(2, worksheet.nrows):
    data = 'str'
    #rad from the second row and so on
    str3 = worksheet.cell_value(row,col0_id)
    str4 = worksheet.cell_value(row,col5_keywords)
    st21 = worksheet.cell_value(row,1)
    st22 = worksheet.cell_value(row,2)
    st23 = worksheet.cell_value(row,3)
    st24 = worksheet.cell_value(row,4)
    st26 = worksheet.cell_value(row,6)
    st27 = worksheet.cell_value(row,7)
    st28 = worksheet.cell_value(row,8)
    st29 = worksheet.cell_value(row,9)
    st210 = worksheet.cell_value(row,10)
    st211 = worksheet.cell_value(row,11)
    st212 = worksheet.cell_value(row,12)
    st213 = worksheet.cell_value(row,13)
    st214 = worksheet.cell_value(row,14)
    st215 = worksheet.cell_value(row,15)
    st216 = worksheet.cell_value(row,16)
    st217 = worksheet.cell_value(row,17)
    st218 = worksheet.cell_value(row,18)
    st219 = worksheet.cell_value(row,19)
    st220 = worksheet.cell_value(row,20)
    
    if str3 == str1:
        str2 = str(str2) + ',' + str(str4)
    else:
        worksheet1.write(rowsheet2, 0,str1)
        worksheet1.write(rowsheet2, 5,str2)
        worksheet1.write(rowsheet2, 1,st1)
        worksheet1.write(rowsheet2, 2,st2)
        worksheet1.write(rowsheet2, 3,st3)
        worksheet1.write(rowsheet2, 4,st4)
        worksheet1.write(rowsheet2, 6,st6)
        worksheet1.write(rowsheet2, 7,st7)
        worksheet1.write(rowsheet2, 8,st8)
        worksheet1.write(rowsheet2, 9,st9)
        worksheet1.write(rowsheet2, 10,st10)
        worksheet1.write(rowsheet2, 11,st11)
        worksheet1.write(rowsheet2, 12,st12)
        worksheet1.write(rowsheet2, 13,st13)
        worksheet1.write(rowsheet2, 14,st14)
        worksheet1.write(rowsheet2, 15,st15)
        worksheet1.write(rowsheet2, 16,st16)
        worksheet1.write(rowsheet2, 17,st17)
        worksheet1.write(rowsheet2, 18,st18)
        worksheet1.write(rowsheet2, 19,st19)
        worksheet1.write(rowsheet2, 20,st20)        
        str1 = str3
        str2 = str4
        st1 = st21
        st2 = st22
        st3 = st23
        st4 = st24
        st6 = st26
        st7 = st27
        st8 = st28
        st9 = st29
        st10 = st210
        st11 = st211
        st12 = st212
        st13 = st213
        st14 = st214
        st15 = st215
        st16 = st216
        st17 = st217
        st18 = st218
        st19 = st219
        st20 = st220

        rowsheet2 = rowsheet2 +1

# to print the last movie
worksheet1.write(rowsheet2, 0,str1)
worksheet1.write(rowsheet2, 5,str2)
worksheet1.write(rowsheet2, 1,st1)
worksheet1.write(rowsheet2, 2,st2)
worksheet1.write(rowsheet2, 3,st3)
worksheet1.write(rowsheet2, 4,st4)
worksheet1.write(rowsheet2, 6,st6)
worksheet1.write(rowsheet2, 7,st7)
worksheet1.write(rowsheet2, 8,st8)
worksheet1.write(rowsheet2, 9,st9)
worksheet1.write(rowsheet2, 10,st10)
worksheet1.write(rowsheet2, 11,st11)
worksheet1.write(rowsheet2, 12,st12)
worksheet1.write(rowsheet2, 13,st13)
worksheet1.write(rowsheet2, 14,st14)
worksheet1.write(rowsheet2, 15,st15)
worksheet1.write(rowsheet2, 16,st16)
worksheet1.write(rowsheet2, 17,st17)
worksheet1.write(rowsheet2, 18,st18)
worksheet1.write(rowsheet2, 19,st19)
worksheet1.write(rowsheet2, 20,st20)
        
        
        
        
