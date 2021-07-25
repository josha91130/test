# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

rain = input("今天有沒有下雨: ")

if rain == '有':
    print("淋著雨")


x = 5
while x <10:
    print('x小於10')
    x = x+1
print('跳出迴圈')
#####################################

while True:
    name = input('請輸入姓名: ')
    if name == 'q':
        break
    else:
        name
########################################
password = '123456'
i = 3

while i > 0:
    pw = input('請輸入密碼: ')
    if pw == password:
        print('登入成功')
        break
    else:
        print('還剩下', i ,'次機會')
        i=i-1





